(function ($) {
  "use strict";
  $(document).ready(function () {
    $("#table-artigos").dataTable({
      "language": {
        "sEmptyTable":     "<span class='alert-info'>&nbsp;<i class='fa fa-info-circle'></i>&nbsp;Nenhum registro encontrado&nbsp;</span>",
        "sInfo":           "Exibindo de _START_ até _END_ de _TOTAL_ registros",
        "sInfoEmpty":      "Nenhum registro para exibir",
        "sInfoFiltered":   " (filtrado de _MAX_ registros)",
        "sInfoPostFix":    "",
        "sInfoThousands":  ",",
        "sLengthMenu":     "<select><option value='10'>10</option><option value='20'>20</option><option value='30'>30</option><option value='40'>40</option><option value='50'>50</option><option value='50'>100</option><option value='-1'>Todos</option></select> registros por página",
        "sLoadingRecords": "Por favor aguarde - carregando...",
        "sProcessing":     "Processando...",
        "sSearch":         "Buscar:",
        "sUrl":            "",
        "sZeroRecords":    "<span class='alert-info'>&nbsp;<i class='fa fa-info-circle'></i>&nbsp;Nenhum registro para exibir&nbsp;</span>",
        "paginate": {
          "first":  "Primeira página",
          "previous": "Anterior",
          "next":     "Próxima",
          "last":     "Última página",
        },
        "decimal": ",",
        "thousands": ".",
      },
      "pagingType": "full_numbers",
      "aoColumns": [ // tabela com 4 colunas
        null, // coluna ordenável
        null,
        null,
        { "bSortable": false } // coluna não ordenável
      ]
    });

    $("#table-fichamentos").dataTable({
      "language": {
        "sEmptyTable":     "<span class='alert-info'>&nbsp;<i class='fa fa-info-circle'></i>&nbsp;Nenhum registro encontrado&nbsp;</span>",
        "sInfo":           "Exibindo de _START_ até _END_ de _TOTAL_ registros",
        "sInfoEmpty":      "Nenhum registro para exibir",
        "sInfoFiltered":   " (filtrado de _MAX_ registros)",
        "sInfoPostFix":    "",
        "sInfoThousands":  ",",
        "sLengthMenu":     "<select><option value='10'>10</option><option value='20'>20</option><option value='30'>30</option><option value='40'>40</option><option value='50'>50</option><option value='50'>100</option><option value='-1'>Todos</option></select> registros por página",
        "sLoadingRecords": "Por favor aguarde - carregando...",
        "sProcessing":     "Processando...",
        "sSearch":         "Buscar:",
        "sUrl":            "",
        "sZeroRecords":    "<span class='alert-info'>&nbsp;<i class='fa fa-info-circle'></i>&nbsp;Nenhum registro para exibir&nbsp;</span>",
        "paginate": {
          "first":    "Primeira página",
          "previous": "Anterior",
          "next":     "Próxima",
          "last":     "Última página",
        },
        "decimal": ",",
        "thousands": ".",
      },
      "pagingType": "full_numbers",
      "aoColumns": [ // tabela com 5 colunas
        null, // coluna ordenável
        null,
        null,
        null,
        { "bSortable": false } // coluna não ordenável
      ]
    });

    $('[data-toggle="tooltip"]').tooltip({
      delay: { show: 500, hide: 100 }
    });

    $('[title="Excluir"]').tooltip({
      delay: { show: 500, hide: 100 }
    });

    $(".alert").alert();

    $(".fancybox").fancybox({
      'width'           : '90%',
      'height'          : '90%',
      'autoScale'       : false,
      'openEffect'      : 'fade',
      'closeEffect'     : 'fade',
      'type'            : 'iframe',
      'overlayOpacity'  : 0.8,
      'overlayColor'    : '#000000'  
    });

  });
})(jQuery)