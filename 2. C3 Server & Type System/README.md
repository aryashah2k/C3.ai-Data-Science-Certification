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
