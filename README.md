# centroid
obliczanie metodą środka ciężkości
class CentroidCalculator:
    """
    Kalkulator centroidy (środka masy) dla wielokąta lub zbioru punktów.
    Jeśli punkty tworzą wielokąt (pierwszy punkt != ostatni), obliczana jest centroida pola (wzór dla wielokąta).
    Gdy pole jest zerowe (np. wszystkie punkty leżą na prostej) zwracany jest średni punkt (arithmetyczny środek).
    """

    def __init__(self, points=None):
        self._pts = []
        if points:
            self.extend(points)

    def add(self, x, y):
        """Dodaj pojedynczy punkt (x, y)."""
        self._pts.append((float(x), float(y)))

    def extend(self, points):
        """Dodaj wiele punktów z iterowalnego obiektu punktów [(x,y), ...]."""
        for p in points:
            self._pts.append((float(p[0]), float(p[1])))

    def centroid(self):
        """
        Zwraca centroidę jako krotkę (Cx, Cy).
        Dla pustej listy zwraca (0.0, 0.0).
        """
        pts = list(self._pts)
        if not pts:
            return 0.0, 0.0

        # Upewnij się, że wielokąt jest zamknięty (pierwszy punkt == ostatni)
        if pts[0] != pts[-1]:
            pts.append(pts[0])

        A = 0.0
        Cx = 0.0
        Cy = 0.0

        for i in range(len(pts) - 1):
            x0, y0 = pts[i]
            x1, y1 = pts[i + 1]
            cross = x0 * y1 - x1 * y0
            A += cross
            Cx += (x0 + x1) * cross
            Cy += (y0 + y1) * cross

        A *= 0.5

        # Jeśli pole jest (praktycznie) zerowe — zwróć średnią arytmetyczną punktów
        if abs(A) < 1e-12:
            n = len(pts) - 1
            if n == 0:
                return 0.0, 0.0
            sx = sum(p[0] for p in pts[:-1])
            sy = sum(p[1] for p in pts[:-1])
            return sx / n, sy / n

        Cx /= (6 * A)
        Cy /= (6 * A)
        return Cx, Cy


if __name__ == "__main__":
    # Przykład użycia
    # Trójkąt o wierzchołkach (0,0), (4,0), (0,3)
    tri = CentroidCalculator([(0, 0), (4, 0), (0, 3)])
    print("Centroida trójkąta:", tri.centroid())

    # Przykład dla współliniowych punktów (zwróci średnią)
    line = CentroidCalculator([(0, 0), (2, 0), (4, 0)])
    print("Środek współliniowych punktów:", line.centroid())
