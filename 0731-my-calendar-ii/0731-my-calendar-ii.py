class MyCalendarTwo:

    def __init__(self):
        self.single_booking = []
        self.double_booking = []

    def book(self, startTime: int, endTime: int) -> bool:
        for db_start, db_end in self.double_booking:
            if max(startTime, db_start) < min(endTime, db_end):
                return False # b/c it gives triple booking 

        for sg_start, sg_end in self.single_booking:
            overlap_start = max(startTime, sg_start)
            overlap_end = min(endTime, sg_end)
            if overlap_start < overlap_end:
                self.double_booking.append((overlap_start, overlap_end))
        self.single_booking.append((startTime, endTime))
        return True
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)