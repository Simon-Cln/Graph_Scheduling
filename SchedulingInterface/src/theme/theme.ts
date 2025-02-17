import { createTheme, ThemeOptions } from '@mui/material/styles';

const getTheme = (mode: 'light' | 'dark'): ThemeOptions => ({
  palette: {
    mode,
    primary: {
      main: '#2196f3',
      light: '#64b5f6',
      dark: '#1976d2',
    },
    secondary: {
      main: '#f50057',
      light: '#ff4081',
      dark: '#c51162',
    },
    background: {
      default: mode === 'light' ? '#f5f5f5' : '#121212',
      paper: mode === 'light' ? '#ffffff' : '#1e1e1e',
    },
  },
  typography: {
    fontFamily: '"NoiGrotesk", "Helvetica", "Arial", sans-serif',
    h1: {
      fontSize: '2.5rem',
      fontWeight: 500,
      fontFamily: '"NoiGrotesk", "Helvetica", "Arial", sans-serif',
    },
    h2: {
      fontSize: '2rem',
      fontWeight: 500,
      fontFamily: '"NoiGrotesk", "Helvetica", "Arial", sans-serif',
    },
    h6: {
      fontSize: '1.25rem',
      fontWeight: 500,
      fontFamily: '"NoiGrotesk", "Helvetica", "Arial", sans-serif',
    },
    body1: {
      fontFamily: '"NoiGrotesk", "Helvetica", "Arial", sans-serif',
    },
    body2: {
      fontFamily: '"NoiGrotesk", "Helvetica", "Arial", sans-serif',
    },
    button: {
      fontFamily: '"NoiGrotesk", "Helvetica", "Arial", sans-serif',
      textTransform: 'none',
    },
  },
  components: {
    MuiCssBaseline: {
      styleOverrides: {
        body: {
          transition: 'all 0.3s ease',
        },
      },
    },
    MuiPaper: {
      styleOverrides: {
        root: {
          transition: 'all 0.3s ease',
        },
      },
    },
    MuiTab: {
      styleOverrides: {
        root: {
          transition: 'all 0.3s ease',
        },
      },
    },
  },
  transitions: {
    duration: {
      shortest: 150,
      shorter: 200,
      short: 250,
      standard: 300,
      complex: 375,
      enteringScreen: 225,
      leavingScreen: 195,
    },
  },
});

export const createAppTheme = (mode: 'light' | 'dark') => createTheme(getTheme(mode));
