$(document).ready( function () {
    $('#table-artigos').dataTable({
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
			"sZeroRecords":    "Nenhum registro para exibir",
			"paginate": {
      			"first": 	 "Primeira página",
      			"previous": "Anterior",
			    "next":     "Próxima",
			    "last":     "Última página",
    		},
    		"decimal": ",",
            "thousands": ".",
    	}, 
    	"pagingType": "full_numbers",
  		"aoColumns": [ // tabela com 8 colunas
		     null, // coluna ordenável
		     null,
		     { "bSortable": false } // coluna não ordenável
	    ]  	
    });

	$('[data-toggle="tooltip"]').tooltip({
    	delay: { show: 500, hide: 100 }
    });

});