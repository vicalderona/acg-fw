$("#enviar").click(function() {

    function validar_correo(correo) {
        var regex = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        return regex.test(correo)
    }

    if ($("#nombre").val().length != 0 && $("#nombre").blur()) {
        $("#mensaje1").hide();
    } else {
        $("#mensaje1").show();
    }
    if ($("#apellido").val().length != 0 && $("#apellido").blur()) {
        $("#mensaje2").hide();
    } else {
        $("#mensaje2").show();
    }
    if (validar_correo($("#correo").val()) && $("#correo").blur()) {
        $("#mensaje3").hide();
    } else {
        $("#mensaje3").show();
    }
    if ($("#consulta").val() != 0 && $("#consulta").blur()) {
        $("#mensaje4").hide();
    } else {
        $("#mensaje4").show();
    }
    if ($("#mensaje").val().length >= 20 && $("#mensaje").blur()) {
        $("#mensaje5").hide();
    } else {
        $("#mensaje5").show();
    }
})





function validar_correo(correo) {
    var regex = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(correo)
}
$("#enviar").click(function() {

    $("#nombre").blur(function() {
        if ($("#nombre").val().length < 3) {
            $("#mensaje1").show();
        } else {
            $("#mensaje1").hide();
        }
    })
    $("#apellido").blur(function() {
        if ($("#nombre").val().length == 0) {
            $("#mensaje2").show();
        } else {
            $("#mensaje2").hide();
        }
    })
    $("#correo").blur(function() {
        if (validar_correo($("#correo").val())) {
            $("#mensaje3").hide();
        } else {
            $("#mensaje3").show();
        }
    })
    $("#consulta").blur(function() {
        if ($("#consulta").val() == 0 || $("#consulta").val() == 0) {
            $("#mensaje4").show();
        } else {
            $("#mensaje4").hide();
        }
    })
    $("#mensaje").blur(function() {
        if ($("#mensaje").val().length < 20) {
            $("#mensaje5").show();
        } else {
            $("#mensaje5").hide();
        }
    })
})

$("#limpiar").click(function() {
    $(".errores").hide();
})