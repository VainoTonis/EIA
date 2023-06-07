""" 
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 
"""
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView
from sqlitestuff import getPIData
from uiElements import createInitialTextItems,createResourceTextItems, initializeConnections, initializePlanetConnections

def main():
        
    app = QApplication([])

    # Create a QGraphicsScene and set the scene rect
    scene = QGraphicsScene(0, 0, 1100, 600)
    # Extract unique planet names and resource names
    piData = getPIData()

    planetTextItems, p0TextItems = createInitialTextItems(scene, piData)
    p1TextItems = createResourceTextItems(scene, piData, "P1", 275)
    p2TextItems = createResourceTextItems(scene, piData, "P2", 450)
    p3TextItems = createResourceTextItems(scene, piData, "P3", 650)
    p4TextItems = createResourceTextItems(scene, piData, "P4", 850)

    initializePlanetConnections(scene, piData, planetTextItems, p0TextItems)

    # Create a QGraphicsView and set the scene
    view = QGraphicsView(scene)
    view.show()

    app.exec()


if __name__ == "__main__":
    main()