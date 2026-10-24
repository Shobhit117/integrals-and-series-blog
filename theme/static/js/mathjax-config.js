window.MathJax = {
  tex: {
    inlineMath: [['\\(', '\\)']],
    displayMath: [['\\[', '\\]']],
    processEscapes: true,
    tags: 'ams',
    tagSide: 'right',
    tagIndent: '0.8em',
    useLabelIds: true
  },
  options: {
    ignoreHtmlClass: '.*|',
    processHtmlClass: 'arithmatex'
  },
  chtml: { scale: 1, matchFontHeight: false },
  startup: {
    pageReady: () => MathJax.startup.defaultPageReady().then(() => {
      const fitInlineMath = () => {
        const equations = document.querySelectorAll('.prose span.arithmatex');
        equations.forEach(equation => equation.classList.remove('wide-inline-math'));
        equations.forEach(equation => {
          const math = equation.querySelector('mjx-container');
          const parent = equation.closest('p, li, .prose');
          if (math && parent && math.getBoundingClientRect().width > parent.clientWidth) {
            equation.classList.add('wide-inline-math');
          }
        });
      };
      fitInlineMath();
      window.addEventListener('resize', fitInlineMath);
    })
  }
};
