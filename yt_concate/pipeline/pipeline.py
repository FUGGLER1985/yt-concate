from .steps.step import StepException

class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs):
        for step in self.steps:
            try:
                step.process()
            except StepException as e:
                print('Exception happened', e)
                break
