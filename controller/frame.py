class Frame:
    @staticmethod
    def set_all_unvisible(ui):
        def setallunvisible():
            ui.frame_new_igel.setVisible(True)

        return setallunvisible

