function one_less(id) {
    location.href = location.href.split("?")[0] + "?name=" + id + "&quantity=-1"
};

function ten_more(id) {
    location.href = location.href.split("?")[0] + "?name=" + id + "&quantity=10"
};