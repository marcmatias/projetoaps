// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable({
    responsive: true,
    // Tradução para pt-br dos controles do DataTable
    "language":{
      "sEmptyTable": "Nenhum registro encontrado",
      "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
      "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
      "sInfoFiltered": "(Filtrados de _MAX_ registros)",
      "sInfoPostFix": "",
      "sInfoThousands": ".",
      "sLengthMenu": "_MENU_ resultados por página",
      "sLoadingRecords": "Carregando...",
      "sProcessing": "Processando...",
      "sZeroRecords": "Nenhum registro encontrado",
      "sSearch": "Pesquisar",
      "oPaginate": {
          "sNext": ">",
          "sPrevious": "<",
          "sFirst": "Primeiro",
          "sLast": "Último"
      },
      buttons: {
        copyTitle: 'Copiado',
        copySuccess: {
            _: '%d linhas copiadas',
            1: '1 linha copiada'
        }
      },
      "oAria": {
          "sSortAscending": ": Ordenar colunas de forma ascendente",
          "sSortDescending": ": Ordenar colunas de forma descendente"
      }
    },
  });
});
