$(document).ready(function(){
    $("td[class*='cpf']").each(function(index, el){
        let cpf = $(el).text()
        $(el).text(cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, "$1.$2.$3-$4"))
    })

    $("td[class*='birth_date']").each(function(index, el){
        let date = new Date($(el).text()).toLocaleDateString()
        $(el).text(date)
    })
});