import math
import svgwrite

class LSystem:
    def __init__(
        self,
        axiom,
        rules,
        iterations,
        branch_length,
        branch_width,
        branch_angle,
        branch_length_falloff,
        leaf_length,
        leaf_width,
        leaf_color,
        branch_color,
        filename,
        size=(800, 800)
    ):
        self.axiom = axiom
        self.rules = dict(rules)
        self.iterations = iterations
        self.branch_length = branch_length
        self.branch_width = branch_width
        self.branch_angle = math.radians(branch_angle)
        self.branch_length_falloff = branch_length_falloff
        self.leaf_length = leaf_length
        self.leaf_width = leaf_width
        self.leaf_color = leaf_color
        self.branch_color = branch_color
        self.filename = filename

        self.instructions = self._create_l_system()
        self._draw_l_system(size)

    def _create_l_system(self):
        """
        Generate L-System instructions based on axiom and rules. 
        Adjust the branching length
        """
        result = self.axiom
        for _ in range(self.iterations):
            result = ''.join(self.rules.get(char, char) for char in result)
            self.branch_length *= self.branch_length_falloff
        return result

    def _draw_l_system(self, size):
        """D
        raw the L-System using svgwrite
        
        Parameters:
        - size: Size of the canvas
        """
            
        drawing = svgwrite.Drawing(self.filename, size=size)
        drawing.add(drawing.rect(insert=(0, 0), size=size, fill="white"))

        x, y = size[0] / 2, size[1]
        angle = -math.pi / 2

        stack = []

        for cmd in self.instructions:
            if cmd == 'F':
                nx = x + math.cos(angle) * self.branch_length
                ny = y + math.sin(angle) * self.branch_length

                drawing.add(
                    drawing.line(
                        start=(x, y),
                        end=(nx, ny),
                        stroke=self.branch_color,
                        stroke_width=self.branch_width
                    )
                )

                x, y = nx, ny

            elif cmd == '+':
                angle += self.branch_angle # turn right

            elif cmd == '-':
                angle -= self.branch_angle # turn left

            elif cmd == '[':
                stack.append((x, y, angle, self.branch_length)) # save current state

            elif cmd == ']': # restore previous state
                # add leaf
                drawing.add(
                    drawing.ellipse(
                        center=(x, y),
                        r=(self.leaf_width, self.leaf_length),
                        fill=self.leaf_color,
                        opacity=0.8
                    )
                )
                x, y, angle, self.branch_length = stack.pop()

        # save
        drawing.save()

