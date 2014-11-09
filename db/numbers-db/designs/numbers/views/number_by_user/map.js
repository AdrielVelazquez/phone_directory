function(doc) {
    if (doc.type == "number" && doc.assigned === true) {
        emit([doc.user, doc._id);
    }
}