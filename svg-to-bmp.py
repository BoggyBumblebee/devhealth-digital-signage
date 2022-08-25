import cairosvg
import wx

class TestFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        cairosvg.svg2png(url="github.com/devhealth-digital-signage/images/badge.svg", 
            write_to="github.com/devhealth-digital-signage//images/badge.png")

        img = wx.Image('github.com/devhealth-digital-signage//images/badge.png')
        # img.ConvertAlphaToMask(255,255,255)
        bmp = wx.Bitmap(img)
        self.Image = wx.StaticBitmap(self, bitmap=bmp)
        self.Image.Bitmap.SaveFile('github.com/devhealth-digital-signage//images/badge.bmp', type=wx.BITMAP_TYPE_BMP)
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(self.Image, 0, wx.ALL, 10)
        self.SetSizer(box)
        self.Fit()
        self.Show()

if __name__ == "__main__":
    app = wx.App()
    frame = TestFrame(None)
    app.MainLoop()