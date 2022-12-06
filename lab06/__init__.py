import numpy as np
from matplotlib import pyplot as plt


def get_proj(u, e_list):
    return sum(map(lambda e: (u @ e) * e, e_list))


print(get_proj(np.array([5, 3, 2]), [np.array([1, 0, 0]), np.array([0, 1, 0])]))


def run():
    fig, axs = plt.subplots(1, 3, subplot_kw={'projection': '3d'})

    funcs = [plot_3d_to_1d, plot_3d_to_2d, plot_3d_to_3d]

    for i in range(len(funcs)):
        funcs[i](axs[i])

    plt.show()


def plot_3d_to_1d(ax):
    u = np.array([5, 3, 2])
    es = [np.array([1, 0, 0])]
    u_proj = get_proj(u, es)
    ax.plot([10, 0, 0], [0, 0, 0])
    ax.scatter([u[0], u_proj[0]],
               [u[1], u_proj[1]],
               [u[2], u_proj[2]], color="red")
    ax.set_title('3d -> 1d')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')


def plot_3d_to_2d(ax):
    u = np.array([5, 3, 2])
    es = [np.array([1, 0, 0]),
          np.array([0, 1, 0])]
    u_proj = get_proj(u, es)
    x = np.arange(0, 10, 0.1)
    y = np.arange(0, 10, 0.1)
    xx, yy = np.meshgrid(x, y, sparse=True)
    z = np.zeros(xx.shape)
    ax.plot_surface(xx, yy, z, alpha=0.6)
    ax.scatter([u[0], u_proj[0]],
               [u[1], u_proj[1]],
               [u[2], u_proj[2]], color="red")
    ax.set_title('3d -> 2d')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')


def plot_3d_to_3d(ax):
    es = [np.array([1, 0, 0]), np.array([0, 1, 0])]
    xx = np.arange(0, 10, 0.1)
    yy = np.arange(0, 10, 0.1)
    a, b = np.meshgrid(xx, yy, sparse=True)
    zz = np.zeros(a.shape)
    x = 5 + 1.5 * np.sin(a) * np.cos(b)
    y = 5 + 1.5 * np.sin(a) * np.sin(b)
    z = 8 + 1.5 * np.cos(a)

    x_proj = np.zeros(x.shape[0])
    y_proj = np.zeros(x.shape[0])
    z_proj = np.zeros(x.shape[0])
    l = zip(x, y, z)
    for i, ar in enumerate(l):
        u = np.array(ar)
        for j in range(u.shape[1]):
            u_proj = get_proj(u[:, j], es)
            x_proj[j] = u_proj[0]
            y_proj[j] = u_proj[1]
            z_proj[j] = u_proj[2]

    ax.plot_surface(a, b, zz, alpha=0.5)
    ax.scatter(x_proj, y_proj, z_proj, marker='.', color='red')
    ax.plot_wireframe(x, y, z)
    ax.set_title('3d -> 3d')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')


run()
