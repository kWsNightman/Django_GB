window.onload = function () {
    $('.basket_list').on('click', 'input[type=number]', function () {
        let t_href = event.target;
        console.log(t_href)
        $.ajax({
            url: "/basket/edit/" + t_href.name + "/" + t_href.value + "/",

            success: function (data) {
                console.log(data.result)
                console.log(data.i)
                $('.basket_count').html(data.i)
                $('.basket_list').html(data.result);

            },
        });
        event.preventDefault();
    });
}