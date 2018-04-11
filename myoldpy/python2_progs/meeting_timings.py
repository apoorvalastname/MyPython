class Room():
   totalrooms = 0
   rooms = []
   def __init__(self,meeting):
      self.roomnumber=Room.totalrooms
      self.endtimeint=meeting.endtimeint
      Room.totalrooms +=1
      Room.rooms.append(self)

   def swap(self,room2):
      x=self.endtimeint
      y=self.roomnumber
      self.endtimeint=Room.rooms[room2].endtimeint
      self.roomnumber=Room.rooms[room2].roomnumber
      Room.rooms[room2].endtimeint=x
      Room.rooms[room2].roomnumber=y

   def heapify(self):
      i=Room.totalrooms-1
      while i>0 and ((Room.rooms)[i].endtimeint)<((Room.rooms)[(i-1)/2].endtimeint):
         (Room.rooms)[i].swap((i-1)/2)
         i =(i-1)/2

   def reheapify(self):
      i=0
      while i<Room.totalrooms and minchild(i) and Room.rooms[minchild(i)].endtimeint < Room.rooms[i].endtimeint:
         minchildroom = minchild(i)
         Room.rooms[i].swap(minchildroom)
         i =minchildroom

   def print_room (self):
      print ' Room : ', self.roomnumber, 'Endtime : ',self.endtimeint

class Meeting():
   def __init__(self, start, end, meetingid):
      self.starttime=start
      self.starttimeint=gettimenum(start)
      self.endtime=end
      self.endtimeint=gettimenum(end)
      self.meetingid=meetingid
      self.room=0

   def get_room(self):
      if not Room.rooms or (self.starttimeint)<(Room.rooms[0].endtimeint):
         room=self.create_new_room()
         self.room=room.roomnumber
      else:
         self.room=Room.rooms[0].roomnumber
         self.edit_minroom()
   
   def print_meeting (self):
      print '  ',self.meetingid,' {:5}'.format(self.starttime),'-', '{:5}{}{}'.format(self.endtime,' Room : ',self.room)

   def create_new_room(self):
      newroom = Room(self)
      newroom.heapify()
      return newroom

   def edit_minroom(self):
      Room.rooms[0].endtimeint=self.endtimeint
      Room.rooms[0].reheapify()

def gettimenum(timestr):
   hrssplit = timestr.split(':')
   hrs = hrssplit[0]
   if int(hrs)<6 :
      hrs = str(int(hrs)+12)
   hrs=hrs+hrssplit[1]
   return hrs

def minchild (roomnum):
   if 2*roomnum+2 > Room.totalrooms-1: 
      if 2*roomnum+1 > Room.totalrooms-1:
         return None
      else:
         return 2*roomnum+1

   if Room.rooms[2*roomnum +1].endtimeint<Room.rooms[2*roomnum +2].endtimeint:
      return (2*roomnum+1)
   else:
      return (2*roomnum+2)
   
def main():
   meetings = [
                Meeting("9:00", "10:30", 'A'),
                Meeting("10:00", "10:30", 'B'),
                Meeting("11:00", "12:00", 'C'),
                Meeting("12:00", "1:30", 'D'),
                Meeting("12:00", "2:00", 'E'),
                Meeting("1:00", "2:00", 'F'),
                Meeting("3:00", "4:00", 'G'),
              ] 
   for m in meetings:
      m.get_room()
   for m in meetings: 
      m.print_meeting()

if __name__ == "__main__":
   main()



