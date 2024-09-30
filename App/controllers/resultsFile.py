from App.models import Result

def import_results(fileID):
    results = Result.query.filter_by(fileID=fileID).all()
    return results
