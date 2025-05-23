from datetime import datetime

class Task:
    # used to generate task IDs
    id_counter = 1

    def __init__(self, num_people, time_period, location_type, 
                location_detail, character, shoot_date_str, task_id = None):
        # unique identifier for each task
        if task_id:
            self.id = task_id
        else:
            self.id = Task.id_counter
            # increment the counter for the next task
        Task.id_counter += 1          
        # actual number of charcaters
        self.num_people = num_people    
        # time period for the task(day, night)
        self.time_period = time_period   
        # type of location (indoor, outdoor)
        self.location_type = location_type  
        # details of the location
        self.location_detail = location_detail  
        # which character to shoot
        self.character = character       
        # date of the shoot
        self.shoot_date = datetime.strptime(shoot_date_str, '%Y-%m-%d')  

        # whether this task is completed or not
        if self.shoot_date < datetime.now():
            self.completed = True
        else:
            self.completed = False

        # calculate the price based on the task details(num_people, time_period, location_type)
        self.price = self.calculate_price()  

    def calculate_price(self):
        # base price
        base_price = 100
        # if total numeber of people is more than 1, add 50 for each additional person
        if self.num_people > 1:
            base_price += (self.num_people - 1) * 50

        # if the time period is night, add 30
        if self.time_period == 'night':
            base_price += 30

        # if the location type is outdoor, add 20
        if self.location_type == 'outdoor':
            base_price += 20
        return base_price
    
    def __str__(self):
        # return the task report
        return f"""Task Summary - T{self.id}
        -------------------------
        number of people  : {self.num_people}
        time period       : {self.time_period}
        location type     : {self.location_type}
        location detail   : {self.location_detail}
        character         : {self.character}
        shoot date        : {self.shoot_date.strftime('%Y-%m-%d')}
        completed         : {self.completed}
        price             : {self.price}
        -------------------------"""
    
    def to_dict(self):
        # convert the task object to a dictionary
        return {
            'id': self.id,
            'num_people': self.num_people,
            'time_period': self.time_period,
            'location_type': self.location_type,
            'location_detail': self.location_detail,
            'character': self.character,
            'shoot_date': self.shoot_date.strftime('%Y-%m-%d'),
            'completed': self.completed,
            'price': self.price
        }
    
    # here we use the static method to convert the dictionary to a task object
    # this is used when we load the tasks from the json file
    @staticmethod
    def from_dict(d):
        return Task(
            num_people=d['num_people'],
            time_period=d['time_period'],
            location_type=d['location_type'],
            location_detail=d['location_detail'],
            character=d['character'],
            shoot_date_str=d['shoot_date'],
            task_id=d['id']
        )


if __name__ == "__main__":
    # new_task = Task(2, 'day', 'indoor', 'studio in sydney', 'Christina', '2025-10-01')
    # print(new_task)
    new_task_2 = Task(3, 'day', 'indoor', 'studio in sydney', 'Christina', '2023-10-01')
    # print(new_task_2)
    # print(new_task_2.to_dict())
    # print(type(new_task_2.from_dict(new_task_2.to_dict())))
    # print(new_task_2.is_due_soon())