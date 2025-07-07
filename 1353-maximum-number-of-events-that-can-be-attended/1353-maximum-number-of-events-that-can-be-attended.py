import heapq

class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        # 1. Sort events by their start day.
        # If start days are the same, the order doesn't strictly matter for correctness
        # with the min-heap, but sorting by end day can be a minor optimization.
        events.sort()

        attended_events = 0
        
        # Min-heap to store the end days of currently available events.
        # We always pick the event that ends soonest to free up the day.
        min_heap = [] 
        
        # Pointer for iterating through the sorted events array.
        event_idx = 0 
        n = len(events)
        
        # Determine the maximum day to iterate up to.
        # This is not strictly needed if we iterate until `min_heap` is empty and `event_idx` reaches `n`.
        # However, it helps set an upper bound for the loop.
        # max_day = 0
        # for _, end_day in events:
        #     max_day = max(max_day, end_day)

        # We can iterate through days from 1 up to the max possible end day (10^5).
        # Or, we can iterate from the first event's start day.
        # A more efficient iteration is to go through each possible day that an event could exist.
        # The loop range from 1 to 10^5 (max endDay) is typically used for these problems.
        # A more precise loop boundary is to go from the minimum start day to the maximum end day.
        
        # Let's use the day counter starting from 1 up to a large enough value
        # or until all events are processed and no more are available.
        
        day = 1 # Start from the first possible day an event can start.
        while day <= 100000 or (event_idx < n and len(min_heap) > 0): # Iterate up to max possible end day
                                                                     # or as long as there are events to process
                                                                     # either from the list or in the heap
            # Add all events that start on the current 'day' to the min_heap.
            while event_idx < n and events[event_idx][0] == day:
                heapq.heappush(min_heap, events[event_idx][1]) # Push end_day to heap
                event_idx += 1
            
            # Remove events from the heap that have already ended before or on the current 'day'.
            # These are events whose end_day is less than the current 'day'.
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            
            # If there are events available to attend on the current 'day' (i.e., heap is not empty),
            # attend the one that ends soonest (top of min_heap).
            if min_heap:
                heapq.heappop(min_heap) # Attend this event (remove it from consideration)
                attended_events += 1
            
            day += 1 # Move to the next day
            
            # Optimization: If all events have been processed from the list
            # and the heap is empty, we can stop early.
            if event_idx == n and not min_heap:
                break
                
        return attended_events