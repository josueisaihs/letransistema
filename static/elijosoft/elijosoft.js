function searching() {
    $.ajax({
        url: "{% url 'view_listteacher' %}",
        type: "POST",
        data: {
            search: $("#id_search").val(),
        },
        success: function (json) {
            var jsoncontent = JSON.parse(json.data);

            var resp = "";
            if (jsoncontent.length > 1){
                resp = "Hemos encontrado " + jsoncontent.length + " coincidencias";
            }
            if (jsoncontent.length === 1){
                resp = "Hemos encontrado una coincidencia";
            }
            if (jsoncontent.length <= 0){
                resp = "No hemos encontrado coincidencias";
            }
            $('#id_search_result').html("<strong class='w3-text-teal'>" + resp + "</strong>");

            var i = 0;
            $('#id_container_teachers').empty();
            $('#id_paginator').hide();
            for (i; i < jsoncontent.length; i++){
                var li = '';
                var icono = "";
                if (jsoncontent[i]['fields']['gender'] === 'm'){
                    icono = "fa-male";
                }else{
                    icono = "fa-female";
                }

                var urledit = '/docencia/editteacher/' + jsoncontent[i]['pk'] + '/';
                var urldelete = '/docencia/delteacher/' + jsoncontent[i]['pk'] + '/';

                li = "<li class=\"w3-padding-16\">\n" +
                    "                    <span onclick=\"\n" +
                    "                        document.getElementById('mensajeModaldelete').innerHTML = " +
                    "'¿Desea eliminar permanentemente al profesor<br><strong>" +
                    jsoncontent[i]['fields']['name'] + " " + jsoncontent[i]['fields']['lastname'] + "</strong> ?';\n" +
                    "                        document.getElementById('aSiModalDelete').href = '" + urldelete + "';\n" +
                    "                        document.getElementById('modalDelete').style.display = 'block';\n" +
                    "                        \"\n" +
                    "                      class=\"w3-padding w3-margin-right w3-medium w3-closebtn w3-hover-text-red\"><i class=\"fa fa-remove\"></i>\n" +
                    "                    </span>\n" +
                    "                    <a href='" + urledit + "'\n" +
                    "                      class=\"w3-padding w3-margin-right w3-medium w3-closebtn w3-hover-text-teal\"><i class=\"fa fa-edit\"></i>\n" +
                    "                    </a>\n<div class=\"w3-row\">\n" +
                    "                        <div class=\"w3-col l1 m1 s2\">" +
                    "                    <img src=\"/" + jsoncontent[i]['fields']['image'] + "\" class=\"w3-left w3-circle w3-margin-right\" style=\"height:50px\"></div>\n" +
                    "                        <div class=\"w3-rest\">\n" +
                    "                    <span class=\"w3-medium\"><i class=\"fa " + icono + " w3-large w3-opacity\"></i><b> " +
                    jsoncontent[i]['fields']['degree'] + " " + jsoncontent[i]['fields']['name'] + " " + jsoncontent[i]['fields']['lastname'] + "</b></span><br>\n" +
                    "                    <span class=\"w3-small\">" + jsoncontent[i]['fields']['title'] + "</span>\n</div></div>" +
                    "                </li>";
                $("#id_container_teachers").append(li);
            }
        },
        error: function (xhr, errmsg, err) {
            $('#id_search_result').html("<strong class='w3-text-red'>Error de conexión</strong>");
        }
    })
}