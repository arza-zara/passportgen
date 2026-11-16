# Finnish Passport Photo Adapter

Straighten, scale, and crop portraits to meet Finnish passport photo requirements in [Poliisin passikuvaohje](https://poliisi.fi/documents/25235045/31329600/Poliisin-passikuvaohje-2020-FI.pdf/d7709348-8248-09a0-8b74-7526e6ee2a5d?t=1600339651285), then arrange them on a printable photo sheet.

## Requirements

The app only needs a modern web browser. No install or build step is required.

## Quick Start

Open `passportgen.html` in a browser.

## How To Use

1. Choose **Open Photo** in slot A.
2. Click the center of one eye, then the center of the other eye.
3. Click the crown of the head, excluding hair.
4. Click the bottom of the chin.
5. Review the result against the guide grid (see below), and adjust brightness
   or contrast if needed.
6. Download the active passport photo, or use **Print Layout** to create a photo
   sheet.

Photo B can be prepared the same way. When both slots are ready, the print sheet
alternates photos A and B.

## Guide Grid

Once all four points are set, the finished photo is shown with the grid from
page 3 of the official guide laid over it:

- **Crown:** the top of the head (without hair) should fall between the two
  upper horizontal lines, 56-84 px (4-6 mm) from the top edge.
- **Chin:** the bottom of the chin should fall between the two lower horizontal
  lines, 96-124 px (7-9 mm) from the bottom edge.
- **Nose:** the face centre line should fall between the two vertical lines,
  at most 21 px (1.5 mm) from the middle of the photo.

The grid carries the same px / mm measurements and brackets as the diagram in
the guide (500 px / 36 mm wide, 653 px / 47 mm high, 56, 28, 445, 28 and 96 px
down the right side, and 42 px and 229 px along the bottom). The px values always
refer to the 500 x 653 px photo, even in the original-pixels export mode. To
leave room for the labels the photo is shown slightly smaller while the grid is
on; on very small screens the labels are left out and only the lines are drawn.

The grid is only a preview aid. It is never added to the downloaded photo or the
print sheet. Use the **Guide grid** checkbox in the toolbar to hide it; the choice
is remembered. If the photo is off the grid, use **Adjust Crop** to place the
points again.

## Output

- Finnish passport photo size: 36 x 47 mm.
- Official export: 500 x 653 px JPEG, compressed to stay under 250 KB when
  possible.
- Original export: JPEG using the source crop resolution, without the official
  pixel or file-size limits.
- Print sheets: 300 DPI JPEG layouts for 9 x 13 cm, 10 x 15 cm, 13 x 18 cm, or a
  single-photo sheet.

## Print Sheet Name

The print-sheet download name can be edited in the **Name** field. By default it
uses:

`Finnish passport photo to print YYYY-MM-DD HH.MM.jpg`

The app adds a `.jpg` extension if needed.

## Privacy

Photos are processed in the browser. The app does not upload photos or use any
external service.

The selected paper size, export mode, guide-grid setting, and side-panel width are saved in browser
local storage. Uploaded photos, crop points, file names, adjustments, and print
sheet names are not saved after reload.
