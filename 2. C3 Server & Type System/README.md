# 2. Introduction to C3 Server and Type System

## A. Logical Architecture: Clusters, Tenants, and Tags

## B. Physical Architecture

## Key Takeaways

- Synchronous computation refers to requests that are made directly from a client to one of the C3 masters, and the response to this request is served directly by the C3 master server. 

- Asynchronous computation refers to the workloads that can be processed and distributed on C3 worker nodes. These requests are received in the form of jobs that the C3 master server puts into a queue. C3 worker nodes pick up the jobs from these queues and perform the necessary computations in the background.


