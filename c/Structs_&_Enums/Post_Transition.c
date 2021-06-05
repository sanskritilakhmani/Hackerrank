/*
We live in a big country. This country has  towns in it. Each town has some post offices in which packages are stored and transferred.

Post offices have different inner structure. Specifically, each of them has some limitations on the packages it can store - their weight should be between  and  inclusively, where  and  are fixed for each office.

Packages are stored in some order in the office queue. That means, that they are processed using this order when sending and receiving.

Sometimes two post offices, even in different towns, may organize the following transaction: the first one sends all its packages to the second one. The second one accepts the packages that satisfy the weight condition for the second office and rejects all other ones. These rejected packages return to the first office back and are stored in the same order they were stored before they were sent. The accepted packages move to the tail of the second office's queue in the same order they were stored in the first office.

You should process several queries in your program. You'll be provided with structures ,  and . in order to complete this task, you should fill the following functions:

 - given the town , print all packages in this town. They should be printed as follows:

Town_name:
    0:
        id_0
        id_1
        ...
    1:
        id_2
        id_3
        ...
    ...
where ,  etc are the numbers of post offices and , ... are the ids of packages from the th post office in the order of its queue, ,  are from the st one etc. There should be one '\t' symbol before post office numbers and two '\t' symbols before the ids.

 - given the towns  and  and post office indices  and , manage the transaction described above between the post office # in town  and the post office # in town .

 - given all towns, find the one with the most number of packages in all post offices altogether. If there are several of them, find the first one from the collection .

 - given all towns and a string , find the town with the name . It's guaranteed that the town exists.

Input Format

First line of the input contains a single integer .  blocks follow, each describing a town.

Every town block contains several lines. On the first line there is a string  - the name of the town. On the second line there is an integer  - the number of the offices in the town.  blocks follow then, each describing an office.

Every office block also contains several lines. On the first line there are three integers separated by single spaces:  (the number of packages in the office),  and  (described above).  blocks follow, each describing a package.

Every package block contains exactly two lines. On the first line there is a string  which is an id of the package. On the second line there is an integer  which is the weight of the package.

Then, there is a single integer  on the line which is the number of queries.  blocks follow, each describing a query.

Every query block contains several lines. On the first line there is an integer ,  or . If this integer is , on the second line there is a string  - the name of town for which all packages should be printed. If this integer is , on the second line there are string , integer , string  and integer  separated by single spaces. That means transactions between post office # in the town  and post office # in the town  should be processed.

If the integer is , no lines follow and the town with the most number of packages should be found.

Constraints

All integer are between  and 
, .
All strings have length 
All towns' names have only uppercase english letters and are unique.
All packages' ids have only lowercase english letters and are unique.
For each post office,   .
All queries are valid, that means, towns with the given names always exist, post offices with the given indices always exist.
Output Format

For queries of type , print all packages in the format provided in the problem statement. For queries of type , print "Town with the most number of packages is " on a separate line.

Sample Input 0

2
A
2
2 1 3
a 2
b 3
1 2 4
c 2
B
1
4 1 4
d 1
e 2
f 3
h 4
5
3
2 B 0 A 1
3
1 A
1 B
Sample Output 0

Town with the most number of packages is B
Town with the most number of packages is A
A:
    0:
        a
        b
    1:
        c
        e
        f
        h
B:
    0:
        d
Explanation 0

Before all queries, town B has  packages in total, town  has . But after transaction all packages from B's th post office go to the st post office of A, except package d because it's too light.
*/

//Post Transition in C - Hacker Rank Solution
#include <stdio.h>
#include <stdlib.h>
#define MAX_STRING_LENGTH 6

struct package
{
   char* id;
   int weight;
};

typedef struct package package;

struct post_office
{
   int min_weight;
   int max_weight;
   package* packages;
   int packages_count;
};

typedef struct post_office post_office;

struct town
{
   char* name;
   post_office* offices;
   int offices_count;
};

typedef struct town town;


void print_all_packages(town t)
{
    printf("%s:\n", t.name);
    for (int i = 0; i < t.offices_count; i++)
    {
        printf("\t%d:\n", i);
        for (int j = 0; j < t.offices[i].packages_count; j++)
            printf("\t\t%s\n", t.offices[i].packages[j].id);
    }
}

void send_all_acceptable_packages(town* source, int source_office_index, town* target, int target_office_index)
{
    int n = 0;
    for (int i = 0; i < source->offices[source_office_index].packages_count; i++)
        if (source->offices[source_office_index].packages[i].weight >= target->offices[target_office_index].min_weight &&
            source->offices[source_office_index].packages[i].weight <= target->offices[target_office_index].max_weight)
            ++n;
    package* newPackages = malloc(sizeof(package)*(n + target->offices[target_office_index].packages_count));
    package* oldPackages = malloc(sizeof(package)*(source->offices[source_office_index].packages_count - n));
    for (int i = 0; i < target->offices[target_office_index].packages_count; i++)
        newPackages[i] = target->offices[target_office_index].packages[i];
    n = target->offices[target_office_index].packages_count;
    int m = 0;
    for (int i = 0; i < source->offices[source_office_index].packages_count; i++)
        if (source->offices[source_office_index].packages[i].weight >= target->offices[target_office_index].min_weight &&
            source->offices[source_office_index].packages[i].weight <= target->offices[target_office_index].max_weight)
        {
            newPackages[n] = source->offices[source_office_index].packages[i];
            ++n;
        }
        else
        {
            oldPackages[m] = source->offices[source_office_index].packages[i];
            ++m;
        }
    target->offices[target_office_index].packages_count = n;
    free(target->offices[target_office_index].packages);
    target->offices[target_office_index].packages = newPackages;
    source->offices[source_office_index].packages_count = m;
    free(source->offices[source_office_index].packages);
    source->offices[source_office_index].packages = oldPackages;
}

int number_of_packages(town t)
{
    int ans = 0;
    for (int i = 0; i < t.offices_count; i++)
        ans += t.offices[i].packages_count;
    return ans;
}

town town_with_most_packages(town* towns, int towns_count)
{
    int ans;
    int max_packages = -1;
    for (int i = 0; i < towns_count; i++)
        if (number_of_packages(towns[i]) > max_packages)
        {
            max_packages = number_of_packages(towns[i]);
            ans = i;
        }
    return towns[ans];
}

town* find_town(town* towns, int towns_count, char* name)
{
    for (int i = 0; i < towns_count; i++)
        if (!strcmp(towns[i].name, name))
            return &(towns[i]);
    return &towns[0];
}

int main()
{
   int towns_count;
   scanf("%d", &towns_count);
   town* towns = malloc(sizeof(town)*towns_count);
   for (int i = 0; i < towns_count; i++) {
      towns[i].name = malloc(sizeof(char) * MAX_STRING_LENGTH);
      scanf("%s", towns[i].name);
      scanf("%d", &towns[i].offices_count);
      towns[i].offices = malloc(sizeof(post_office)*towns[i].offices_count);
      for (int j = 0; j < towns[i].offices_count; j++) {
         scanf("%d%d%d", &towns[i].offices[j].packages_count, &towns[i].offices[j].min_weight, &towns[i].offices[j].max_weight);
         towns[i].offices[j].packages = malloc(sizeof(package)*towns[i].offices[j].packages_count);
         for (int k = 0; k < towns[i].offices[j].packages_count; k++) {
            towns[i].offices[j].packages[k].id = malloc(sizeof(char) * MAX_STRING_LENGTH);
            scanf("%s", towns[i].offices[j].packages[k].id);
            scanf("%d", &towns[i].offices[j].packages[k].weight);
         }
      }
   }
   int queries;
   scanf("%d", &queries);
   char town_name[MAX_STRING_LENGTH];
   while (queries--) {
      int type;
      scanf("%d", &type);
      switch (type) {
      case 1:
         scanf("%s", town_name);
         town* t = find_town(towns, towns_count, town_name);
         print_all_packages(*t);
         break;
      case 2:
         scanf("%s", town_name);
         town* source = find_town(towns, towns_count, town_name);
         int source_index;
         scanf("%d", &source_index);
         scanf("%s", town_name);
         town* target = find_town(towns, towns_count, town_name);
         int target_index;
         scanf("%d", &target_index);
         send_all_acceptable_packages(source, source_index, target, target_index);
         break;
      case 3:
         printf("Town with the most number of packages is %s\n", town_with_most_packages(towns, towns_count).name);
         break;
      }
   }
   return 0;
}


