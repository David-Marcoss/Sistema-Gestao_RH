function utilizou_hora_extra(id){
    
    console.log(id)
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
   
    $.ajax(
        {
            type: 'POST',
            url: '/hora-extra/Utilizar-horas-extra/'+ id + '/',
            data: {csrfmiddlewaretoken: token},
            
            success: function(result){
                console.log("Funcionou")
                $("#mensagem").text(result.mensagem)
            }
        }
    );

}