from .models import Organisation, Project, User, TimelineItem

def create_tables():
    Organisation.create_table()
    Project.create_table()
    User.create_table()
    TimelineItem.create_table()
