import weechat

weechat.register("Tabs", "jimble", "0.1", "DWTFYWWI ver4.20", "Buffer tabs", "", "")

def tabs_item_callback(data, item, window):
    return "my content | "

bar_item = weechat.bar_item_new("bar_item_tabs", "tabs_item_callback", "")
bar_tabs = weechat.bar_new("tabs", "off", "100", "root", "", "top", "horrizontal", "vertical", "1", "1", "default", "default", "default", "on", "bar_item_tabs")
