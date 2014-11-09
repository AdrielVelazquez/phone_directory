function(doc) {
    if (doc.type == "number") {
        emit([doc.assigned, doc._id], doc)
    }
}