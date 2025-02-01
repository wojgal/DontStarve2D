class Animation:
    def __init__(self, frames, frame_duration):
        self.frames = frames
        self.num_frames = len(self.frames)
        self.frame_duration = frame_duration
        self.current_frame = 0
        self.time_elapsed = 0


    def update(self, dt):
        self.time_elapsed += dt

        if self.time_elapsed >= self.frame_duration:
            self.time_elapsed = 0
            self.current_frame = (self.current_frame + 1) % self.num_frames


    def get_current_frame(self):
        return self.frames[self.current_frame]
    

    def reset_animation(self):
        self.current_frame = 0


    def get_timer(self) -> int:
        return self.frame_duration * self.num_frames