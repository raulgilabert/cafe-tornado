function q_one_less(id) {
    location.href = location.href.split("?")[0] + "?name=" + id + "&quantity=-10&data=q"
};

function q_ten_more(id) {
    location.href = location.href.split("?")[0] + "?name=" + id + "&quantity=10&data=q"
};

function m_one_less(id) {
    location.href = location.href.split("?")[0] + "?name=" + id + "&quantity=-10&data=m"
};

function m_ten_more(id) {
    location.href = location.href.split("?")[0] + "?name=" + id + "&quantity=10&data=m"
};