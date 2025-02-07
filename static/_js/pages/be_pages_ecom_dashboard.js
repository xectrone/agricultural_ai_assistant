/*
 *  Document   : be_pages_ecom_dashboard.js
 *  Author     : pixelcave
 *  Description: Custom JS code used in eCommerce Dashboard Page
 */

// Chart.js Charts, for more examples you can check out http://www.chartjs.org/docs
class pageEcomDashboard {
  /*
   * Init Charts
   *
   */
  static initOverviewChart() {
    // Set Global Chart.js configuration
    Chart.defaults.color = '#818d96';
    Chart.defaults.scale.grid.color = 'transparent';
    Chart.defaults.scale.grid.zeroLineColor = 'transparent';
    Chart.defaults.scale.beginAtZero = true;
    Chart.defaults.elements.point.radius = 0;
    Chart.defaults.elements.point.hoverRadius = 0;
    Chart.defaults.plugins.tooltip.radius = 3;
    Chart.defaults.plugins.legend.labels.boxWidth = 12;

    // Get Chart Container
    let chartOverviewCon = document.getElementById('js-chartjs-overview');

    // Set Chart Variables
    let chartOverview, chartOverviewOptions, chartOverviewData;

    // Overview Chart Options
    chartOverviewOptions = {
      responsive: true,
      maintainAspectRatio: false,
      tension: .4,
      scales: {
        y: {
          suggestedMin: 0,
          suggestedMax: 600
        }
      },
      interaction: {
        intersect: false,
      },
      plugins: {
        tooltip: {
          callbacks: {
            label: function (context) {
              return '$ ' + context.parsed.y;
            }
          }
        }
      }
    };

    // Overview Chart Data
    chartOverviewData = {
      labels: ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'],
      datasets: [
        {
          label: 'This Week',
          fill: true,
          backgroundColor: 'rgba(6, 101, 208, .5)',
          borderColor: 'transparent',
          pointBackgroundColor: 'rgba(6, 101, 208, 1)',
          pointBorderColor: '#fff',
          pointHoverBackgroundColor: '#fff',
          pointHoverBorderColor: 'rgba(6, 101, 208, 1)',
          data: [369, 255, 420, 330, 460, 160, 350]
        },
        {
          label: 'Last Week',
          fill: true,
          backgroundColor: 'rgba(6, 101, 208, .2)',
          borderColor: 'transparent',
          pointBackgroundColor: 'rgba(6, 101, 208, .2)',
          pointBorderColor: '#fff',
          pointHoverBackgroundColor: '#fff',
          pointHoverBorderColor: 'rgba(6, 101, 208, .2)',
          data: [270, 460, 290, 231, 419, 450, 280]
        }
      ]
    };

    // Init Overview Chart
    if (chartOverviewCon !== null) {
      chartOverview = new Chart(chartOverviewCon, {
        type: 'line',
        data: chartOverviewData,
        options: chartOverviewOptions
      });
    }
  }

  /*
   * Init functionality
   *
   */
  static init() {
    this.initOverviewChart();
  }
}

// Initialize when page loads
Dashmix.onLoad(() => pageEcomDashboard.init());
