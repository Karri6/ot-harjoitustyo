import tkinter as tk

# generoitu koodi alkaa (poislukien docstring kommentit)
class PillarChart(tk.Canvas):
    """
    A generated (or greatly fixed) class that creates the pillar chart
    using data from the data it's passed
    """
    def __init__(self, master, max_chart_height, *args, **kwargs):
        """
        Constructor for the class

        Args:
            master: widget where the chart is imposed to
            max_chart_height: chart maximum height
            *args: non keyworded variables for the gui settings
            *kwargs: keyworded variables for the gui settings
        """
        super().__init__(master, *args, **kwargs)
        self.months = []
        self.data = []
        self.max_chart_height = max_chart_height
        self.chart_width = self.winfo_reqwidth() - 20
        self.bar_width = 30
        self.bar_spacing = 50

    def update_data(self, months, data):
        """
        Draws a new chart using the months and data it's fed

        Args:
            months: months being displayed
            data: workout data from the months
        """
        self.months = months
        self.data = data
        self.draw_chart()

    def draw_chart(self):
        """
        Draws the Pillar Chart

        Returns: 
            None, If no is data present, chart is not drawn
        """
        self.delete("all")
        if not self.data:
            return
        max_data = max(self.data)

        if max_data == 0:
            max_data = 20

        scale_factor = self.max_chart_height / max_data
        for i, month in enumerate(self.months):
            x0 = i * (self.bar_width + self.bar_spacing) + 50
            y0 = self.max_chart_height + 20
            x1 = x0 + self.bar_width
            y1 = y0 - self.data[i] * scale_factor

            if self.data[i] < 10:
                fill_color = '#fa5757'
            elif 10 <= self.data[i] <= 15:
                fill_color = '#f0d341'
            else:
                fill_color = '#64f588'

            self.create_rectangle(x0, y0, x1, y1, fill=fill_color)
            self.create_text((x0 + x1) / 2, y0 + 10, text=month)
            self.create_text((x0 + x1) / 2, y1 - 10, text=str(self.data[i]))

# generoitu koodi päättyy