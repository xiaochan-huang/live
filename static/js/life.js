$(function () {
    $('.checkLife').click(function () {
            $('.checkLife').addClass("active");
            $('.addLife').removeClass("active");
            $('.delLife').removeClass("active");
            $('.updateLife').removeClass("active");
            $('.lifelist').show();
            $('.lifeadd').hide();
            $('.lifedel').hide();
            $('.lifeupdate').hide();
        }
    );
    $('.addLife').click(function () {
            $('.checkLife').removeClass("active");
            $('.addLife').addClass("active");
            $('.delLife').removeClass("active");
            $('.updateLife').removeClass("active");
            $('.lifelist').hide();
            $('.lifeadd').show();
            $('.lifedel').hide();
            $('.lifeupdate').hide();
        }
    );
    $('.delLife').click(function () {
            $('.checkLife').removeClass("active");
            $('.addLife').removeClass("active");
            $('.delLife').addClass("active");
            $('.updateLife').removeClass("active");
            $('.lifelist').hide();
            $('.lifeadd').hide();
            $('.lifedel').show();
            $('.lifeupdate').hide();
        }
    );
    $('.updateLife').click(function () {
            $('.checkLife').removeClass("active");
            $('.addLife').removeClass("active");
            $('.delLife').removeClass("active");
            $('.updateLife').addClass("active");
            $('.lifelist').hide();
            $('.lifeadd').hide();
            $('.lifedel').hide();
            $('.lifeupdate').show();
        }
    );
});

function addLife(_this) {
    var life= $(_this).parent().parent();
    var life_id = life.find("[name='id']").val();
    var date = life.find("[name='date']").val();
    var consumption_matters = life.find("[name='consumption_matters']").val();
    var amount = life.find("[name='amount']").val();
    var total = life.find("[name='total']").val();

    $.ajax({
        url: "",
        type: "post",
        data: {
            date: date,
            consumption_matters: consumption_matters,
            amount: amount,
            total: total
        },
        success: function (result) {
            alert(result.data);
            location.reload()
        },
        error: function () {
            alert("数据发送失败!");
        }
    });
}

function delLife(_this) {
    var life= $(_this).parent().parent();
    var life_id = life.find("[name='id']").val();
    $.ajax({
        url: "",
        type: "delete",
        data: JSON.stringify({
            id: life_id
        }),
        success: function (result) {
            alert(result.data);
            location.reload()
        },
        error: function () {
            alert("数据发送失败!");
        }
    });
}

function putLife(_this) {
    var life= $(_this).parent().parent();
    var life_id = life.find("[name='id']").val();
    var date = life.find("[name='date']").val();
    var consumption_matters = life.find("[name='consumption_matters']").val();
    var amount = life.find("[name='amount']").val();
    var total = life.find("[name='total']").val();
    $.ajax({
        url: "",
        type: "put",
        data: JSON.stringify({
            id:life_id,
            date: date,
            consumption_matters: consumption_matters,
            amount: amount,
            total: total
        }),
        success: function (result) {
            alert(result.data);
            location.reload()
        },
        error: function () {
            alert("数据发送失败!");
        }
    });
}