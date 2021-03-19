import numpy as np


def ReadObj(path):
    with open(path) as f:
        lines = [line.rstrip().split(' ') for line in f]
    # filter v,f to list
    lst_v = []
    lst_f = []
    for line in lines:
        if line[0] == 'v':
            lst_v.append(list(map(float, list(line[1:]))))
        elif line[0] == 'f':
            # remove vn from f then append to list f
            lst_f.append(list(map(int, list([val.split('/')[0] for val in line[1:]]))))
    return lst_v, lst_f


def GetCanvas2DCoor(vertices, padding=0.1):
    vertices = np.array(vertices)
    # add 10% more space between face and outer frame
    x_max = max(vertices[:, 0]) + (max(vertices[:, 0]) - min(vertices[:, 0])) * padding
    x_min = min(vertices[:, 0]) - (max(vertices[:, 0]) - min(vertices[:, 0])) * padding
    y_min = min(vertices[:, 1]) - (max(vertices[:, 1]) - min(vertices[:, 1])) * padding
    y_max = max(vertices[:, 1]) + (max(vertices[:, 1]) - min(vertices[:, 1])) * padding
    return [x_min, y_max], [x_max, y_min]


def GetCenterCoor(vertices):
    vertices = np.array(vertices)
    center_x = sum(vertices[:, 0]) / len(vertices[:, 0])  # avg of x
    center_y = sum(vertices[:, 1]) / len(vertices[:, 1])  # avg of y
    center_z = sum(vertices[:, 2]) / len(vertices[:, 2])  # avg of z
    return [center_x, center_y, center_z]


def CalTriangleArea(v1, v2, v3):
    x2subx1 = v2[0] - v1[0]
    y3suby1 = v3[1] - v1[1]
    x3subx1 = v3[0] - v1[0]
    y2suby1 = v2[1] - v1[1]
    return abs(x2subx1 * y3suby1 - x3subx1 * y2suby1) / 2


class NewObj:

    def __init__(self, vertices, faces):
        self.vertices = vertices
        self.faces = faces

    def __repr__(self):
        return f'Obj({len(self.vertices)} vertices, {len(self.faces)} faces)'

    def SaveObj(self, path, write_faces=True):
        with open(path, 'w') as f:
            for vert in self.vertices:
                print(f"v {' '.join(str(v) for v in vert)}", file=f)
            if write_faces:
                for face in self.faces:
                    print(f"f {' '.join(str(fa) for fa in face)}", file=f)
        print('Saved')
