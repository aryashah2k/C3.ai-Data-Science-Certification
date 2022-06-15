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
