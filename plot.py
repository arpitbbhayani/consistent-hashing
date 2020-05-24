import matplotlib.pyplot as plt

def plot_hashring(ring_length, occupied_keys, nodes, item_key: int = None, node_key: int = None):
    figure = plt.figure()
    axes_1 = figure.add_axes([0, 0, 3, 1])
    axes_1.axes.get_yaxis().set_visible(False)

    y_data = [0] * ring_length
    for k in occupied_keys:
        y_data[k] = 1

    if item_key:
        y_data[item_key] = 0.75

    barlist = axes_1.bar(range(ring_length), y_data, color="grey")

    if item_key is not None:
        barlist[item_key].set_color('g')

    if node_key is not None:
        barlist[node_key].set_color('r')

    i = 0
    for k, rect in enumerate(barlist):
        height = rect.get_height()
        if i < len(occupied_keys) and occupied_keys[i] == k:
            text = nodes[i].name
            i += 1
        else:
            text = ""
        axes_1.annotate(text,
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')

    plt.show()
