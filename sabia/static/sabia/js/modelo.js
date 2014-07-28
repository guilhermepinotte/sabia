$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip({
	    delay: { show: 500, hide: 100 }
	});
//	$('[data-toggle="popover"]').popover({
//	    delay: { show: 500, hide: 100 }
//	});	
	
});

//Adicionar mais um campo
function addcampo(form){
	qtd=$('#qtdcampos').val();
	qtd++;
	if(form=='edit'){
		//Se no formulário de editar
		bloco = '<div class="row bs-callout bs-callout-warning boxcampo" style="padding: 10px 0 0 0; margin: 0 0 15px 0" id="'+qtd+'"><input type="hidden" id="campoid'+qtd+'" name="campoid'+qtd+'" value="camponovo"> <div class="col-sm-5"><div class="form-group" ><label for="exampleInputEmail1">Campo:</label><input type="text" class="form-control" id="camponome'+qtd+'" name="camponome'+qtd+'" placeholder="Nome do campo"></div></div><div class="col-sm-6"><div class="form-group"><label for="exampleInputEmail1">Descrição:</label><textarea  class="form-control" id="campodescricao'+qtd+'" name="campodescricao'+qtd+'" placeholder="Descrição" style="resize:vertical;"></textarea></div></div><div class="col-sm-1" style="text-align: right; padding: 0 15px 0 0; margin: 0 0 10px 0" ><a class="btn btn-xs btn-danger apagar" href="javascript:apagarCampo('+qtd+')" id="'+qtd+'"><i class="glyphicon glyphicon-trash"></i> Apagar</a></div></div>';
	}else{
		//Se no Formulário de 
		bloco = '<div class="row bs-callout bs-callout-warning boxcampo" style="padding: 10px 0 0 0; margin: 0 0 15px 0" id="'+qtd+'"><div class="col-sm-5"><div class="form-group" ><label for="exampleInputEmail1">Campo:</label><input type="text" class="form-control" id="camponome'+qtd+'" name="camponome'+qtd+'" placeholder="Nome do campo"></div></div><div class="col-sm-6"><div class="form-group"><label for="exampleInputEmail1">Descrição:</label><textarea  class="form-control" id="campodescricao'+qtd+'" name="campodescricao'+qtd+'" placeholder="Descrição" style="resize:vertical;"></textarea></div></div><div class="col-sm-1" style="text-align: right; padding: 0 15px 0 0; margin: 0 0 10px 0" ><a class="btn btn-xs btn-danger apagar" href="javascript:apagarCampo('+qtd+')" id="'+qtd+'"><i class="glyphicon glyphicon-trash"></i> Apagar</a></div></div>';
	}
			
	$('.boxcampos').append(bloco).slideDown('slow');
	$('#camponome'+qtd).focus();
	$('#qtdcampos').val(qtd);	
}

//APAGAR Campo - CriarModelo
function apagarCampo(id){		
	linha = $(".boxcampo[id="+id+"]");
	linha.slideUp('speed',function(){$(this).remove()});
}	
function excluirModelo(id){
	linha = $(".linhamodelo[id="+id+"]");
	estilo = linha.css("background-color");
	linha.css("background-color","#FFE0E0");
	if(confirm("Deseja realmente apagar este modelo?")){
		//APAGAR
		linha.css("background-color","#F0F5FF");
		$.post('/sabia/fichamentos/modelos/ajaxmodelo',{op:"apagar-modelo",modeloid:id},function(r){
			if(r=="True"){
				linha.slideUp("slow",function(){$(this).remove()});
			}else{
				linha.css("background-color",estilo);
				alert("Não foi possível apagar este campo.");
			}			
		});		
	}else{
		//Não
		linha.css("background-color","white");
	}
}
function excluirCampo(id,campoid){
	linha = $(".boxcampo[id="+id+"]");
	estilo = linha.css("background-color");
	linha.css("background-color","#FFE0E0");
	if(confirm("Deseja apagar permanentemente este campo?")){
		//APAGAR
		linha.css("background-color","#F0F5FF");
		$.post('/sabia/fichamentos/modelos/ajaxmodelo',{op:"apagar-campo",campoid:campoid},function(r){
			if(r=="True"){
				linha.slideUp("speed",function(){$(this).remove()});
			}else{
				linha.css("background-color",estilo);
				alert("Não foi possível apagar este campo.")
			}			
		});
	}else{
		//Não
		linha.css("background-color",estilo);
	}
}
function validarModelo(form){
	
	if ($("#modelonome").val()==""){
		alert('Infome o Nome do Modelo');
		$("#modelonome").focus();
		return false;
	}
//	if ($("#modelodescricao").val()==""){
//		alert('Infome uma descrição para o Modelo');
//		$("#modelodescricao").focus();
//		return false;
//	}
	
	qtd = $("#qtdcampos").val();	
	for (i=1;i<=qtd;i++){		
		if ($("#camponome"+i).val()==""){
			alert('Infome o nome do campo');
			$("#camponome"+i).focus();
			return false;
		}	
	}
	return true;
}
