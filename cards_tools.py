# 记录所有的名片字典
card_list = []


def show_menu():

    """显示菜单"""
    print("*" * 50)
    print("欢饮使用[名片管理系统] V 1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)


def new_card():

    """新增名片"""
    print("-" * 50)
    print("功能：新增名片")

    # 1. 提示用户输入名片的详细信息
    name_str = input("请输入姓名： ")
    phone_str = input("请输入电话： ")
    qq_str = input("请输入QQ： ")
    email_str = input("请输入邮箱： ")

    # 2. 使用用户输入的名片信息建立一个名片字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}

    # 3. 将名片字典添加到列表中
    card_list.append(card_dict)
    # print(card_list)

    # 4. 提示用户添加成功
    print("提示：成功添加 %s 的名片" % name_str)


def show_all():

    """显示全部"""
    print("-" * 50)
    print("功能：显示全部")

    # 判断是否存在名片记录，如果没有，提示用户并且返回
    if len(card_list) == 0:

        print("提示：没有任何名片记录")

        # return 返回函数的执行结果，下方代码不会执行
        # 如果 return 后面没有任何内容，会返回到调用函数的位置，并且不返回任何结果
        return

    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:

        print(name, end="\t\t")

    print("")

    # 打印分割线
    print("-" * 50)

    # 遍历名片列表依次输出字典信息
    for card_dict in card_list:

        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                           card_dict["phone"],
                                           card_dict["qq"],
                                           card_dict["email"]))


def search_card():

    """查询名片"""
    print("-" * 50)
    print("功能：查询名片")

    # 1. 提示用户要搜索的姓名
    find_name = input("请输入要搜索的姓名： ")

    # 2. 遍历名片列表，查询要搜索的姓名，如果没有找到，需要提示用户
    for card_dict in card_list:

        if card_dict["name"] == find_name:

            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("-" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                               card_dict["phone"],
                                               card_dict["qq"],
                                               card_dict["email"]))

            deal_card(card_dict)

            break

    else:

        print("提示：抱歉，没有找到 %s" % find_name)


def deal_card(find_dict):

    """
    处理查找到的名片
    :param find_dict: 查找到的名片
    """
    print(find_dict)

    action_str = input("请输入对名片的操作:"
                       "1. 修改/ 2. 删除/ 0. 返回上级菜单")

    if action_str == "1":

        find_dict["name"] = input_card_info(find_dict["name"], "姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ：")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱：")
        print("修改名片成功")

    elif action_str == "2":

        card_list.remove(find_dict)

        print("删除名片成功！")


def input_card_info(dict_value, tip_message):

    """
    输入名片信息
    :param dict_value: 字典中原有的值
    :param tip_message: 输入的提示文字
    :return: 如果用户输入了内容，就返回内容，否则返回字典中原有的值
    """

    # 1. 提示用户输入内容
    result_str = input(tip_message)

    # 2. 针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:

        return result_str

    # 3. 如果用户没有输入内容，返回字典中原有的值
    else:

        return dict_value
