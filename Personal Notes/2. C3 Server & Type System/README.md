# 2. Introduction to C3 Server and Type System

## A. Logical Architecture: Clusters, Tenants, and Tags

## B. Physical Architecture

## Key Takeaways

- Synchronous computation refers to requests that are made directly from a client to one of the C3 masters, and the response to this request is served directly by the C3 master server. 

- Asynchronous computation refers to the workloads that can be processed and distributed on C3 worker nodes. These requests are received in the form of jobs that the C3 master server puts into a queue. C3 worker nodes pick up the jobs from these queues and perform the necessary computations in the background.

## C. Jobs, Queues, and Nodes

Like many platforms, the C3 AI Suite uses queues and jobs to manage work for processing and nodes to process work.

Here is a quick overview of these concepts:

**Jobs: A unit of work that needs to be done.** 

For example:
- Provisioning Type metadata
- Ingesting data from a file
- Normalizing time series data

**Queues: Lists of related jobs.** 

For example:
- Batch jobs
- Cron jobs which are chronological jobs that run at scheduled times or intervals

**Nodes: Units of processing power**

- What does the work
- Master nodes manage
- Worker nodes process

You can think of queues as task checklists for related tasks.

![queue-info]()

All of our queues are based on the idea that when data changes, or is invalidated, they must be reprocessed. 

So we call our queues invalidation queues. Three of the 12+ invalidation queues are shown to the right.

There are two categories of nodes in the platform:

- Master Nodes manage work by doing "house cleaning" to make sure work gets passed through.
- giving priority to important tasks.

For example, they make sure that user interface tasks are not delayed by long-running processing tasks.
- Worker Nodes perform calculations as they pick up jobs from queues and process them in first-in-first-out order.

![nodes-info]()

There is one master node and many worker nodes for each tenant. Tags share queues and processing resources with other tags on their tenant.

When a large job is kicked off, the master node can spin up more worker nodes (up to a specified limit) and spin them down when the job is done.

![large-job]()

### What does all this mean?

Queues and jobs allow three features of data processing:

- Asynchronicity: Many jobs can be run at the same time and as resources become available.

i.e multiple queues for different related tasks

- Parallelism: The same job can be divided among and run on multiple worker nodes.

- Multiple worker nodes work on one job.

- Each worker has many threads that can each work on a different job or task.

For example, in our training environments, each worker node has 8 threads.

- Autoscaling: Processing resources can be added or removed as needed.

i.e. spinning up/down of worker nodes on demand

### Do I have to do anything to manage jobs, queues, and nodes?

Generally no. 

However, you will write ML training jobs from a higher level API, and you may (will) need this knowledge for troubleshooting purposes. 

**Refresher**

- C3 server uses queues to distribute the Jobs to worker nodes.

- In synchronous processing, the C3 master server alone is responsible to receive, retrieve, compute, and serve the submitted request.

- For computations that need a long processing time, asynchronous processing is recommended.

- C3 server supports spinning the number of workers up or down as needed.

## D. C3.ai Type System

Add Documentation

## Platform Types

The C3 AI Platform has over 4000 Types already built-in. These provide methods for handling most use cases we have seen in over ten years of building applications with customers. 

Some important Types include:

1. Parametric Types
- Types that take inputs or outputs as parameters
- This is a category of Types — there is no Type called parametric

2. Persistable Types
- Can store data in tables
- Include methods to store and retrieve the data
- Persistable Type is also a parametric Type (takes an input parameter)

## Type Inheritance

Inheritance is a key principle of object-oriented programming. 

In the C3 AI Type System, we use mixins to pass fields and methods from parent to child Types. 

With mixins, you can "mix in" functionality (field/attribute values, methods) from existing, already built Types into new Types that you build yourself — rather than recoding that functionality from scratch.

## Fields, Methods, and Annotations

Types are created with fields, methods, and annotations. 

### Fields

Fields store the actual values on a single instance of an object. Each field in a Type has a field declaration. There are many categories of fields but we will mainly use these three: 

- Primitive fields hold values of basic (or primitive) objects like integer, string, and boolean, as well as some more complex objects like datetime. A primitive field in a C3 AI Type is comparable to a value cell in a datatable. 
- Collection fields represent a list of foreign key references from another Type filtered based on a key for this Type. A collection field in a C3 AI Type looks comparable to an array in a datatable cell when fetched, but it's useful to know that this array is not stored -- the array is generated on the fly and is actually pulled in as a run-time query when the data is fetched. 
- Reference fields contain a pointer or a foreign key reference to an instance of another Type.

### Methods

A method is a function that is associated with a Type, has a name, and implements some action. It can take arguments as input, perform logic, invoke changes (for example, change database state), and return values to the caller.

Below are some examples of what methods can do:

- calculate and return the number of apartments in a building
- calculate and return an array of all lightbulb instances that are currently on
- run complex analytical operations and write the results back to a datatable

A method is defined in a Type declaration. Declaring a method is the same as declaring a field on a Type that has a value Type of a function. In the signature of the function, developers specify the input parameters, output parameters, implementation language, and execution location.

Methods are ubiquitous throughout an application; they're used in the UI, with metrics, background processes, task scheduler, and so on. They are everywhere and play a very important role for ML models on the C3 AI platform. You will learn how to implement and use methods throughout this course. 

### Annotations

Annotations are used to further configure the Types themselves and the fields on them. Think of annotations as defining how something should be. Annotations can be defined for Types and/or fields where necessary. 

There are a few annotations you will need in this course, such as:

1. @pythonEnv: This annotation is used to implement methods on a Type where the method function is written in Python. (The default language expected by the C3 server is JavaScript!)
2. @db: These annotations are used for database specifications.
3. @ts:  These annotations are used to specify how time series data should be treated during normalization.

## E. Persistable Types

Add Documentation

## F. Naming Conventions

It is important to learn and use the right naming conventions in the C3 AI Type system. Let's see how we should name Types, fields, schemas, and Type keys. 

1. Type name

- Type names use PascalCase, also called UpperCamelCase
- Unique in package and chain of dependencies
- Very descriptive with no abbreviations

2. Field Name
          
- Field names use camelCase (first letter lower case)
- Very descriptive with no abbreviations
- Use plurals for collection fields

3. Schema Name

- Schema names use upper snake case, i.e. 
  - ALL CAPS separated by an underscore
  - using abbreviations by removing all non-leading vowels

For example; 

"Apple Sauce" --> "APPL_SC"

"SmartBulb Measurements" --> "SMRTBLB_MSRMNTS"

- Unique in their package and chain of dependencies
- Limited to 19 characters — so keep them as short as possible

4. Type Key Name

- Same naming convention as schema name
- Unique in the extendable Type
- Best practice: under 15 characters 

Here is an easy reference for Type, field, schema and Type key names in their own naming conventions.

![reference-type]()

```
Note:

If you see the word Type with a capitalized first letter in this course, it is referring to a C3 AI Type. 

If you see the word type in all lower case, it is referring to a class or category of something. We try to avoid using it this way but in some cases it is unavoidable.
```
## F. Entity Relationship Diagram

An Entity Relationship Diagram (ERD) in the C3 Type system is a graphical representation of the relationship among Application Data Model Types, which are persistable Types.  

Let's take a look at how we use Application Data Model Types, relate them to each other, and present them in an ERD. 

Here, we will use a small part of the use case you will work on throughout this course. 

![erd-1]()

We have smart lightbulbs (we will call them smartbulbs) that are installed in fixtures, which are in apartments, which are in buildings.  

![erd-2]()

Fixture.csv data file contains data on fixture, apartment, building, latitude, and longitude.

If you look closely, you will see that the relationship between apartments and buildings is listed more than once. The latitude and longitude, which are unique to each building, are also recorded many times. 

To reduce data redundancy and improve data integrity, we create relational databases that are structured in normal forms. (What are normal forms?)

Refer: https://en.wikipedia.org/wiki/Database_normalization

For example, we want relationships and data to be recorded in only one place so that it can be updated or deleted in one place. This makes sure that changes are consistent throughout our data model, and a change in one place do not result in inconsistencies elsewhere.

We need to decide how to represent that data in the application data schema. To conform to normal forms, we split the data between three C3 Types (Fixture, Apartment, and Building) and connect them to each other through reference and collection fields.

![erd-3]()

Here, let's take a closer look at the collection and reference fields in this ERD. 

There are many fixtures in each apartment. The fixtures field in Apartment Type represents the ids of all the fixtures in an apartment using the apartment field in Fixture Type as a filter field. This makes the fixtures field in Apartment Type a collection field. 

Each fixture is installed in an apartment. The apartment field in Fixture Type holds the id of the (individual) Apartment in which that fixture is installed. This makes the apartment field in Fixture type a reference field. 

The id fields of all Types, and latitude and longitude fields in the Building Type, are defined as primitive fields.

![erd-4]()

### Relationships in ERD

The four common relationships you will see in the ERD of the C3 AI application you will use in this course are many-to-one, one-to-many, one-to-one, and many-to-many as shown in the image on the right. 

![erd-5]()

Did you recognize the many-to-one and one-to-many relationships? Those are the types of relationships for collection and reference fields respectively. 

You might be asking where we see one-to-one and many-to-many relationships. 

For example, at any specific time, one bulb can be only in one fixture. This creates a one-to-one relationship between a bulb and a fixture. However, over a period of time, many bulbs might take place in many fixtures creating a many-to-many relationship between bulbs and fixtures.

What do we use these relationships for other than creating normals forms? Utilizing this structure, you can navigate an ERD! 

### Navigating an ERD using Dot Notation

You might be familiar with dot notation from some programming languages such as JavaScript. Don't worry if you are not!

In a programming language, dot notation is a way to access a property of an object. To reach a property in an object, you need to write the name of the object, followed by a dot (.), and then followed by the name of the property. In an ERD of a C3 AI application, Types can be considered as objects and fields can be considered as properties. 

Outside of the C3 Type system, you can reach a property of an object but you can not reach from one object to property of another object. In the C3 Type system, using dot notation, you can create a path to navigate from a source Type to a field in another Type utilizing the field relationships such as reference and collection. In this context, the source Type can be defined as the Type that your path starts from. 

But how can we create that path? 

There are three main steps in determining a path:

- Choose the source Type. 
- Determine where the data you want to reach is located. 
- Utilize the field connections that can take you from the source Type to the data you need to reach.

Let's practice creating a path using the ERD below. This ERD is a somewhat more complex version of the one you saw before. 

![erd-6]()

Let's say we want to create a path from SmartBulb Type to the power field in the SmartBulbMeasurement Type.

In determining the path, it is helpful to consider the data model. SmartBulb has a collection field called bulbMeasurements which is linked to the SmartBulbMeasurementSeries Type. In that Type, there is another collection field called data which is connected to the SmartBulbMeasurement, the Type that contains the desired field — power. Then, the path from SmartBulb Type to the power field in the SmartBulbMeasurement Type is: 

```
bulbMeasurements[SmartBulb] -> data[SmartBulbMeasurementSeries] -> power[SmartBulbMeasurement]
```
With dot notation, it would be bulbMeasurements.data.power

