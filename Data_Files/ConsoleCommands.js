//Exploring the C3 Console
c3ShowType(MyType)
c3Grid(MyType.fetch())

// get the server number/version from console
Cluster.hosts()[0].pkgName

// show the tenant, tag, and host URL
c3Grid(c3Context())

//List all packages on a Tag
c3Grid(TagMetadataStore.packages())

// get all the Types in a particular package
c3Grid(TagMetadataStore.typesByPackage("lightbulbPM"))

// monitoring data uploads
c3Grid(SourceFile.get("SourceFile_id_from_fetch.csv").sourceStatus()) // status of the whole file
c3Grid(SourceStatus.fetch()) // status of individual chunks

//Check C3 Queues
c3Grid(InvalidationQueue.countAll())

//Check Queue Errors
c3Grid(MapReduceQueue.errors())

//Attempt recovering failed jobs
MapReduceQueue.recoverFailed()

//Clear errors in a given Queue
c3QErrorsClear(MapReduceQueue)
