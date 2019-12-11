function PaginadorControl(name, contenedor, contenedorContenido, elemt=20) {
    this.name = name;
    this.contenedor = contenedor;
    this.items = [];
    this.elemt = elemt;
    this.contenedorContenido = contenedorContenido;

    this.currentIndex = 0;
    this.step = 0;

    this.stepCorection = function (length, elemt) {
        const stepFloat = length / elemt;
        const stepInt = stepFloat.toFixed(0);

        if (stepInt - stepFloat > 0){
            return stepInt;
        }else{
            return new Number(stepInt) + 1;
        }
    };

    this.paginatorConstructor = function(items) {
        this.items = items;
        this.step = this.stepCorection(this.items.length, this.elemt);

        var el = $("#" + this.contenedor);
        el.empty();
        el.append("<li class='paginatorPrevius'><a role='button' onclick='" + this.name + ".paginatorSet(0);'>&#xf100</a></li>");
        el.append("<li class='paginatorPrevius'><a role='button' onclick='" + this.name + ".paginatorPrevius();'>&#10094</a></li>");

        const index = this.currentIndex + 1;
        el.append("<li id='id_refPag_" + this.name + "'><a role='switch'>" + index + " de " + this.step + "</a></li>");

        el.append("<li class='paginatorNext'><a role='button' onclick='" + this.name + ".paginatorNext();'>&#10095</a></li>");
        el.append("<li class='paginatorNext'><a role='button' onclick='" + this.name + ".paginatorEnd();'>&#xf101</a></li>");

        this.paginatorSet(0);
    };

    this.paginatorEnd = function () {
      this.paginatorSet(this.step);
    };

    this.paginatorPrevius = function () {
        if (this.currentIndex > 0){
          this.currentIndex--;
        }
        this.paginatorSet(this.currentIndex);
    };

    this.paginatorNext = function () {
        if (this.currentIndex < (this.step - 1)){
          this.currentIndex++;
        }

        this.paginatorSet(this.currentIndex);
    };

    this.paginatorSet = function (n) {
        n = n === this.step ? (this.step - 1) : n;

        this.currentIndex = n;
        var el = $("#" + this.contenedorContenido);
        el.empty();

        var i = this.currentIndex * this.elemt;
        var max = this.currentIndex * this.elemt + this.elemt;

        if (max > this.items.length){
            max = this.items.length;
        }

        for (i; i < max; i++){
            el.append(this.items[i]);
        }

        const index = this.currentIndex + 1;
        $("#id_refPag_" + this.name).html("<a role='switch'>" + index + " de " + this.step + "</a>");
    };
}

var ItemObject = function (pk, name, lastname, space=" ") {
      this.pk = pk;
      this.name = name;
      this.lastname = lastname;
      this.selected = false;

      this.full = this.name + space + this.lastname;
    };

var ListObjects = function (name, contenedor, controlSelect) {
    this.name = name;
    this.contenedor = $("#" + contenedor);
    this.list = [];
    this.contenedorList = "";
    this.controlSelect = controlSelect;
    this.paginador = undefined;
    this.elementLimit = 10;
    this.buttonOptional = "";

    this.append = function (teacher) {
        this.list.push(teacher);
    };

    this.agregar =  function () {
        this.contenedor.empty();
      const contenido = "" +
          "<div class='w3-border w3-round-large w3-padding es-shadow'>" +
          "     <div class='w3-tiny w3-row'>" +
          "         " + this.buttonOptional +
          "         <input id='id_input_" + this.name + "' class=\"w3-threequarter w3-input w3-round w3-border es-shadow\"" +
          "         onkeyup=\"" + this.name + ".buscar($(this).val().toLowerCase())\" type=\"text\"" +
          "         placeholder=\"Buscar ...\" value=\"\">" +
          "     </div><br>" +
          "    <div id=\"id_list_" + this.name + "\">" +
          "    </div>" +
          "    <div class=\"w3-center\">\n" +
          "         <ul class=\"w3-pagination w3-tiny\" id=\"id_paginator_" + this.name + "\"></ul>\n" +
          "    </div>" +
          "</div>";
      this.contenedor.append(contenido);

      this.paginador = new PaginadorControl(this.name + ".paginador", "id_paginator_" + this.name, "id_list_" + this.name, this.elementLimit);

      this.contenedorList = $("#id_list_" + this.name);
      this.llenarLista(this.list);
    };

    this.buscar = function (val) {
        this.llenarLista(
            this.list.filter(
                function(item){
                    return (item.name.toLowerCase().indexOf(val) > -1 || item.lastname.toLowerCase().indexOf(val) > -1)
            })
        );
    };

    this.llenarLista = function (list) {
        this.contenedorList.empty();
        var name = this.name;
        if (list.length > 0){
            this.paginador.paginatorConstructor(
                list.map(
                    function (item) {
                        return ("" +
                            "<div " +
                            "   onclick='" + name + ".selected(" + item.pk + ", \"" + item.full + "\")' " +
                            "   class='w3-small w3-hover-light-gray w3-text-gray' " +
                            "   role='button'>" +
                            "   <div class='w3-row'>" +
                            "       <div class='w3-col l1 m1 s1 class_" + name +"_check' id='id_item_" + name + "_" + item.pk + "'>" +
                                        (item.selected ? "<i class='fa fa-check w3-text-green'></i>" : "<p> </p>")  +
                            "       </div>" +
                            "       <div class='w3-rest'>" + item.full + "</div>" +
                            "   </div>" +
                            "</div>");
                    }
                )
            );
        }else{
            this.contenedorList.append("<div class='w3-text-red w3-opacity'><p><i class='fa fa-exclamation-triangle'</i> Ninguna coincidencia</p></div>");
        }

    };

    this.selected = function (pk, text) {
        console.log(text);
        $(".class_" + name +"_check").html("<p> </p>");
        $("#id_item_" + this.name + "_" + pk).empty().append("<i class='fa fa-check w3-text-green'></i>");
        this.list.map(function (item) {
            item.selected = item.pk === pk ? !item.selected : false;
        });

        this.buscar($("#id_input_" + this.name).val());

        document.getElementById(this.controlSelect).options.selectedIndex = 0;
        for (let i = 0; i < document.getElementById(this.controlSelect).options.length; i++){
            if (document.getElementById(this.controlSelect).options[i].text.toLowerCase().indexOf(text.toLowerCase()) > -1){
                document.getElementById(this.controlSelect).options.selectedIndex = i;
                break;
            }
        }
    }
};


var CursoControl = function (pk, titulo, open, deadline, selectControl, image, description, ci, minYear, maxYear) {
    this.selectControl = selectControl;
    this.pk = pk;
    this.ci = ci;
    this.titulo = titulo;
    this.description = description;
    this.openline = new Date(open);
    this.deadline = new Date(deadline);
    this.image = image;
    this.description = description;
    this.minYear = minYear;
    this.maxYear = maxYear;

    this.isOpen = function () {
        const now = new Date();
        return (now >= this.openline && now <= this.deadline)
    };

    this.yearsOldAccess = function () {
      const years = new Date(this.ci[2] + this.ci[3] + "/" + this.ci[4] + this.ci[5] + "/" + this.ci[0] + this.ci[1]);
      const now = new Date();
      const edad = new Number((now - years) / (365 * 24 * 60 * 60 * 1000));
      return edad >= this.minYear && edad <= this.maxYear;
    };
};


var CursosConteainer = function (name, contenedor, cursosControl) {
    this.name = name;
    this.contenedor = contenedor;
    this.cursosControl = cursosControl;

    this.agregar = function () {
        this.llenar(this.cursosControl);
    };

    this.filterTitle = function (title) {
      this.llenar(this.cursosControl.filter(function (cursoControl) {
          if (cursoControl.titulo.toLowerCase().indexOf(title.toLowerCase()) > -1){
              return cursoControl
          }
      }));
    };

    this.llenar = function (lista) {
        let contenedor = $("#" + this.contenedor);
        contenedor.empty();
        if (lista.length < 1){
            contenedor.append("<p class='w3-margin w3-opacity w3-text-red w3-leftbar w3-border-red w3-padding'>No hay cursos disponibles</p>")
        }else{
            lista.map(function (cursoControl) {
                if (cursoControl.isOpen()){
                    contenedor.append(
                        "<div class=\"w3-third w3-card-8\" style='width: 25%; margin: 0.5%;' id='id_" + cursoControl.titulo + "'>\n" +
                        "   <img width='100%' src='" + cursoControl.image + "' alt='Imagen Cursos'>" +
                        "   <div class='w3-container w3-center w3-padding'>" +
                        "       <h4 class=''>" + cursoControl.titulo + "</h4></<br>\n" +
                        (cursoControl.isOpen() ?
                            ( cursoControl.yearsOldAccess() ?
                        "       <input type=\"button\" class=\"w3-btn w3-teal w3-border-bottom w3-round-large\"\n" +
                        "           value=\"SOLICITAR\"\n" +
                        "           onclick=\"" + cursoControl.selectControl + ".selectedIndex('" + cursoControl.titulo + "');" +
                        "                  submit();\"/>"
                                : "<p class='w3-leftbar w3-border-red w3-rightbar w3-text-red'><b>NO CUMPLE LOS REQUISITOS DE EDAD</b></p>" )
                            : "<p class='w3-leftbar w3-border-red w3-rightbar w3-text-red'><b>CERRADO</b></p>" ) +
                        "   </div>\n" +
                        "</div>"
                    );
                }
            });
        }
    };
};


var SelectControl = function (id) {
    this.id = id;

    this.selectedIndex = function (text) {
        document.getElementById(this.id).options.selectedIndex = 0;
        for (let i = 0; i < document.getElementById(this.id).options.length; i++){
            if (document.getElementById(this.id).options[i].text.toLowerCase().indexOf(text.toLowerCase()) > -1){
                document.getElementById(this.id).options.selectedIndex = i;
            }
        }
    };
};

var Candidate = function () {
  this.name;
  this.pk;
  this.lastname;
  this.interview;
  this.selected;
  this.show = true;
  this.groupPk;
  this.urlCarnet;

  this.interviewCheck = function (text1="checked", text2="") {
      if (this.interview)
          return text1;
      else
          return text2;
  };

  this.selectCheck = function () {
      if (this.selected)
          return "checked";
      else
          return "";
  };
};

var CandidateControl = function (nombre, contenedor, urlInterview, urlSelected, interviewFilter, selectedFilter,
                                 search) {
  this.candidates = new Array();
  this.contenedor = $("#" + contenedor);
  this.nombre = nombre;

  this.urlInterview = urlInterview;
  this.urlSelected = urlSelected;

  this.interviewFilter = document.getElementById(interviewFilter);
  this.selectedFilter = document.getElementById(selectedFilter);

  this.searchInput = search;

  this.addCandidate = function (candidate) {
    this.candidates.push(candidate);
  };

  this.buscador = function () {
      const interview_Filtre = this.interviewFilter.checked;
      const selected_Filtre = this.selectedFilter.checked;

      const text = this.searchInput.val().toString().toUpperCase();

      this.agregar(
        this.candidates.filter(
            function (candidate) {
                let show = true;

                if (candidate.name.toUpperCase().indexOf(text) > -1 || candidate.lastname.toUpperCase().indexOf(text) > -1)
                    show = show && true;
                else
                    show = show && false;

                if (interview_Filtre){
                    if (candidate.interview)
                        show = show && true;
                    else
                        show = show && false;
                }

                if (selected_Filtre){
                    if (candidate.selected)
                        show = show && true;
                    else
                        show = show && false;
                }

                return show;
            }
        )
      );
  };

  this.agregar = function (lista) {
      var contenedor = this.contenedor.empty();
      var nombre = this.nombre;

      lista.map(
          function (candidate) {
              var contenido = "" +
                  "<div class=\"w3-card-2 w3-row w3-padding w3-margin nombre-candidato\">\n" +
                  "    <div class=\"w3-threequarter\">\n" +
                  "        <a role=\"button\" class=\"w3-text-black w3-padding\" onclick=\"alert('Hola');\">\n" +
                  "            <i class=\"fa fa-file\"></i> " + candidate.name + " " + candidate.lastname  +
                  "        </a>\n" +
                  "    </div>\n" +
                  "    <div class=\"w3-quarter w3-row-padding\">\n" +
                  "        <div class=\"w3-half w3-container w3-center\">\n" +
                  "            <span class=\"w3-opacity w3-small\">Entrevista</span><br>\n" +
                  "            <label class=\"es-switch w3-small\">\n" +
                  "                 <input type=\"checkbox\" onchange=\"" + nombre + ".interviewChange(" + candidate.pk + ", $(this))\"\n" +
                  "                     " + candidate.interviewCheck() + ">\n" +
                  "                 <div class=\"es-slider es-round\"></div>\n" +
                  "            </label>\n" +
                  "        </div>\n" +
                  "        <div class=\"w3-half w3-container w3-center\">\n" +
                  "            <div  id=\"id_selected_" + candidate.pk  + "\" style=\"display: " + candidate.interviewCheck("block", "none") + ";\">\n" +
                  "                <span class=\"w3-opacity w3-small\">Seleccionado</span><br>\n" +
                  "                <label class=\"es-switch w3-small\">\n" +
                  "                     <input id=\"id_selected_checked_" + candidate.pk + "\"\n" +
                  "                         type=\"checkbox\" onchange=\"" + nombre + ".selectedChange(" + candidate.pk + ", $(this))\"\n" +
                  "                     " + candidate.selectCheck() + ">\n" +
                  "                     <div class=\"es-slider es-round\"></div>\n" +
                  "                </label>\n" +
                  "            </div>\n" +
                  "        </div>\n" +
                  "    </div>\n" +
                  "</div>";

              contenedor.append(contenido);
          }
      );
  };

  this.interviewChange = function(pk, el) {
        $.ajax({
            url: this.urlInterview,
            type: "POST",
            data: {
                candidate: pk,
            },
            success: function (json) {
                if (JSON.parse(json.data)){
                    document.getElementById("id_selected_" + pk).style.display = "block";
                    el.checked = true;
                }else {
                    document.getElementById("id_selected_" + pk).style.display = "none";
                    el.checked = false;
                    document.getElementById("id_selected_checked_" + pk).checked = false;
                }

                this.candidates = this.candidates.map(
                    function (candidate) {
                        if (candidate.pk === pk)
                            candidate.interview = el.checked;
                    }
                );
            },
            error: function (xhr, errmsg, err) {
                // $('#id_candidate_edit_flag').html("<strong class='w3-text-red'>Error de conexión</strong>");
            }
        });
  };

  this.recomendedChange = function(pk, el) {
        $.ajax({
            url: this.urlRecommended,
            type: "POST",
            data: {
                candidate: pk,
            },
            success: function (json) {
                if (JSON.parse(json.data))
                    el.checked = true;
                else
                    el.checked = false;

                this.candidates = this.candidates.map(
                    function (candidate) {
                        if (candidate.pk === pk)
                            candidate.recommended = el.checked;
                    }
                );
            },
            error: function (xhr, errmsg, err) {
                // $('#id_candidate_edit_flag').html("<strong class='w3-text-red'>Error de conexión</strong>");
            }
        });
  };

  this.selectedChange = function(pk, el) {
        $.ajax({
            url: this.urlSelected,
            type: "POST",
            data: {
                candidate: pk,
            },
            success: function (json) {
                if (JSON.parse(json.data))
                    el.checked = true;
                else
                    el.checked = false;

                this.candidates = this.candidates.map(
                    function (candidate) {
                        if (candidate.pk === pk)
                            candidate.selected = el.checked;
                    }
                );
            },
            error: function (xhr, errmsg, err) {
                // $('#id_candidate_edit_flag').html("<strong class='w3-text-red'>Error de conexión</strong>");
            }
        });
  }
};

var Group = function (pk, name) {
    this.pk = pk;
    this.name = name;
};


var CandidateToGroup = function (nombre, contenedor, urlSelect, coursePk) {
    this.nombre = nombre;
    this.contenedor = $("#" + contenedor);
    this.candidates = new Array();
    this.groups = new Array();
    this.urlSelect = urlSelect;
    this.coursePk = coursePk;

    this.addCandidate = function (candidate) {
        this.candidates.push(candidate);
    };

    this.addGroup = function (group) {
        this.groups.push(group);
    };

    this.agregar = function (lista) {
        const nombre = this.nombre;
        var contenedor = this.contenedor;
        var groups = this.groups;
        var urlCarnet = this.urlCarnet;

        var groupList = function (pk) {
            var str = "";
            var exist = false;
            groups.map(function (group) {
                str += "<option value='" + group.pk + "' " + ((pk === group.pk) ? "selected" : "") + ">" + group.name + "</option>";
                exist = exist || (pk === group.pk);
            });

            str += "<option value='0' class='w3-opacity' " + ((exist === true) ? "" : "selected") + " disabled>Seleccionar Grupo</option>";

            return str;
        };

        contenedor.empty();

        lista.map(function (candidate) {
            var contenido = "" +
            "<tr class=\"w3-row\">" +
            "    <td class=\"w3-half\">" + candidate.name + " " + candidate.lastname +
            "    </td>" +
            "    <td class=\"w3-quarter\"><a target='_blank' role='button' class='w3-text-black' href='" + candidate.urlCarnet + "'><i class='fa fa-address-card'></i></a></td>" +
            "    <td class=\"w3-quarter\">\n" +
            "        <select onchange=\"" + nombre + ".selectGroup(" + candidate.pk + ", this.options[this.selectedIndex].value)\"" +
            "                class=\"w3-select w3-border w3-validate w3-round es-shadow\">" +
                groupList(candidate.groupPk) +
            "        </select>" +
            "    </td>" +
            "</tr>";

            contenedor.append(contenido);
        });
    };

    this.selectGroup = function (candidatePk, groupPk) {
         $.ajax({
            url: this.urlSelect,
            type: "POST",
            data: {
                group: groupPk,
                candidate: candidatePk,
                course: this.coursePk,
            },
            success: function (json) {
                console.log("Ok");
            },
            error: function (xhr, errmsg, err) {
                console.error(errmsg, err);
            }
        });
    };
};

function selectValue(id, value=true) {
    if (value){
        return document.getElementById(id).options[document.getElementById(id).selectedIndex].value;
    }else{
        return document.getElementById(id).options[document.getElementById(id).selectedIndex].innerText;
    }
}