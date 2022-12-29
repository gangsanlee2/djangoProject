import os
import platform
myos = platform.system()
root = r"C:\Users\bitcamp\PycharmProjects\djangoProject"
def dir_path(param):
    if (param == "algorithms") :
        return os.path.join(root, "basic", param)
    elif (param == "aitrater") \
            or (param == "dc_gan") \
            or (param == "fashion") \
            or (param == "fruits") \
            or (param == "iris") \
            or (param == "lstm") \
            or (param == "mnist_number") :
        return os.path.join(root, "basic", "dlearn", param)
    elif (param == "bicycle") \
            or (param == "crime") \
            or (param == "etc") \
            or (param == "midwest") \
            or (param == "mpg") \
            or (param == "oklahoma") \
            or (param == "stroke") \
            or (param == "titanic") :
        return os.path.join(root, "basic", "mlearn", param)
    elif (param == "imdb") \
            or (param == "samsung_report") :
        return os.path.join(root, "basic", "nlp", param)
    elif (param == "pythonic") :
        return os.path.join(root, "basic", param)
    elif (param == "cnn") \
            or (param == "mosaic"):
        return os.path.join(root, "basic", "vision", param)
    elif (param == "webcrawler") :
        return os.path.join(root, "basic", param)
    elif (param == "krx") :
        return os.path.join(root, "basic", "webcrawler", param)
    elif (param == "comments") \
            or (param == "z_posts") \
            or (param == "b_users") \
            or (param == "tags") \
            or (param == "views"):
        return os.path.join(root, "blog", param)
    elif (param == "cinmas") \
            or (param == "movies") \
            or (param == "showtimes") \
            or (param == "theater_tickets") \
            or (param == "theaters"):
        return os.path.join(root, "movie", param)
    elif (param == "z_users") \
            or (param == "z_posts"):
        return os.path.join(root, "security", param)
    elif (param == "carts") \
            or (param == "categories") \
            or (param == "deliveries") \
            or (param == "orders") \
            or (param == "products"):
        return os.path.join(root, "shop", param)

if __name__ == '__main__':
    print(">> "+dir_path("carts"))