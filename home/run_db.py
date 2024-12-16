from .models import Student

def student():
    '''
    model = Student(name="Saptaswa", id=2)
    print(model.name)
    model.save()
    '''
    '''
    model=Student.objects.all()
    for _ in  model:
        print(f"id: {_.id} and name: {_.name}")
    #print(model)
    '''
    '''
    model=Student.objects.get(id=2)
    model.marks=40
    model.save()
    '''

