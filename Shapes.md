<!-- [![ART](logo.png)](Home) -->

## Area masks: creating polygonal shapes
*(By Jean-Christophe Frisch)*

### A step-by-step tutorial

`[B1]` = Left mouse button
`[B3]` = Right mouse button
‌

1. Create a new polygon shape by clicking on the " *Add Polygon* " button. This will enable the on preview editing to let you create the shape.
2. `Ctrl + Click[B1]` in the preview to create the first point. At this point, you can already drag it if you want. The shape list will display the number of point in the shape.
3. `Ctrl + Click[B1]` to create the second point. Now you see the first line of the cage, represented as a dashed line, but still no closed polygon, because you need at least three points to have a valid, closed shape. An orange line appears, explanation in the next step.
4. `Ctrl + Click[B1]` to create the third point. Now you see the polygon with a white solid line, surrounded by a black solid line. This is the real shape that will limit the effect of the tool. The orange line has also moved. This line is the "Insertion line", and by default, connects the last point of the cage to its first point (it's the closing segment). The 2 points at each end of the orange line shows the extremities of the Insertion line.
5. Move your cursor away from the shape, and `Ctrl + Click[B1]` to add a point. The new point is taking place *inside* the Insertion line, i.e. at the end of the points list.
6. Move over a segment of the polygon: the Insertion line is now under the cursor, which mean that point creation will take place there, between those new previous and next point.
7. Stay over the segment and `Ctrl + Drag[B1]`: the new point is created where the insertion line was. Of course, once the point is created, you can release the Ctrl key while still dragging the point. For your convenience, the points and the insertion line are hidden during the adjustment.
8. Move the cursor over a point. Hints: you may need to move over a segment first to make the extremity points appear. Once your mouse is over a point, this point becomes orange (the orange element is the selected element). The two other points shows now the previous and next points.
9. You can drag the point to adjust it
10. While still over the point, use `Shift + Drag[B1]` to the right. This will let you adjust the roundness of that corner. When dragging to the left, it will go back to a sharp corner. Each point can be rounded. As you can see, if you go all the way right, the curve start at the previous point and end at the next point. You can also use the scroll wheel instead, while over the point to adjust. Scroll up (your finger moves away from you) to round the corner (it moves away from the point), and vice versa.
11. Repeat this step on the previous point, set the roundness to the maximum. Now you can see that, because the previous point is still to it's minimum value, the curve start straight to this previous point. However both the currently edited point and the previously edited point has maximum roundness. In this case, the connection of the curve to the cage segment is done in the middle of the dashed segment. But with different roundness values, it can end up anywhere inside this segment. Changing the roundness value have an impact in the previous and next sub-curve, and it can look awkward at first sight, but there's some tips to make thing easy.
12. You can move over a segment and `Drag[B1]` to move it
13. You can move over a segment and `Shift + Drag[B1]` to move the entire shape
14. The polygon shape should still be selected in the Shape list, so click on the `+` icon on the right. This button will create a shape of similar type to the one actually selected. Make sure that the *On preview editing* button is still active (it should be)
15. Now add 4 points in this new shape to create a big square BUT you'll press `Shift + Ctrl + Click[B1]` to create the points. This will create points with roundness value to the maximum, and you'll end up with something more like a circle than a square. Each roundness value can still be edited.
16. Move over a point and `Ctrl + [B3]` to delete a point. ART won't delete the 3 last points. If you want to delete a shape entirely, you'll have to do that through the Shape list (`-` button).

### Creating "predictable" shapes

It's very simple: just alternatively create points with sharp corners (roundness = 0, by using the `Ctrl` modifier key at creation time) and points with totally round corners (roundness = 100, by using the `Ctrl + Shift` modifier key at creation time). You end up with a series of Bezier curves of degree 3. The sharp points should be located on the *border* you want to draw, and the *round points* are used to control the curvature, so it won't usually be on the border.
