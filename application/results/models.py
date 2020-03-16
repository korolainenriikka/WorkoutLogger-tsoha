from application import db

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    # materiaalissa lisäks nää:
    # date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    # onupdate=db.func.current_timestamp())

    #näihin ois kiva saada rajoituksia, esim weight 0-300, 50g jaollinen tai 2,5 kg mut voi rajottaaliikaa
    movement = db.Column(db.String(144), nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float)

    def __init__(self, name, reps, weight):
        self.name = name
        self.reps = reps
        self.weight = weight
