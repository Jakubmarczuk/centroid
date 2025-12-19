class CentroidCalculator:
    def __init__(self, points=None):
        self._pts = []
        if points:
            self.extend(points)
    def add(self, x, y):
        self._pts.append((float(x), float(y)))
    def extend(self, points):
        for p in points:
            self._pts.append((float(p[0]), float(p[1])))
    def centroid(self):
        pts = list(self._pts)
        if not pts:
            return 0.0, 0.0
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