def import_info(info, des=None):
    with open('tablet.csv', 'a+') as file:
        if des == None:
            for i in info:
                file.write(f"{i}\n")
            file.write(f"\n")
        else:
            file.write(des.join(info))
            file.write(f"\n")