import React, { useState, useRef } from 'react';
import { 
  Container, 
  Paper, 
  Typography, 
  Box, 
  Alert,
  Tabs,
  Tab,
  AppBar,
  Toolbar,
  IconButton,
  Drawer,
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  useTheme,
  Divider,
  CssBaseline,
  ThemeProvider,
  Fade,
  Switch,
  FormControlLabel
} from '@mui/material';
import {
  Menu as MenuIcon,
  FileUpload as FileUploadIcon,
  Timeline as TimelineIcon,
  TableChart as TableChartIcon,
  Assessment as AssessmentIcon,
  Info as InfoIcon,
  Brightness4 as DarkModeIcon,
  Brightness7 as LightModeIcon
} from '@mui/icons-material';
import { createAppTheme } from './theme/theme';
import FileSelector from './components/FileSelector';
import GraphDisplay from './components/GraphDisplay';
import MatrixDisplay from './components/MatrixDisplay';
import CalendarDisplay from './components/CalendarDisplay';
import CriticalPathDisplay from './components/CriticalPathDisplay';
import GraphControls from './components/GraphControls';
import PDFExport from './components/PDFExport';
import TabPanel from './components/TabPanel';
import { GraphData } from './types/graphTypes';

function App() {
  const [graphData, setGraphData] = useState<GraphData | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [currentTab, setCurrentTab] = useState(0);
  const [drawerOpen, setDrawerOpen] = useState(false);
  const [darkMode, setDarkMode] = useState(false);
  const [zoom, setZoom] = useState(1);
  const [viewMode, setViewMode] = useState<'timeline' | 'tree'>('timeline');
  const [showCriticalPath, setShowCriticalPath] = useState(false);

  const theme = useTheme();
  const appTheme = createAppTheme(darkMode ? 'dark' : 'light');

  // Refs for PDF export
  const graphRef = useRef<HTMLDivElement>(null);
  const matrixRef = useRef<HTMLDivElement>(null);
  const calendarRef = useRef<HTMLDivElement>(null);

  const handleFileSelect = async (file: File) => {
    try {
      setError(null);
      const formData = new FormData();
      formData.append('file', file);

      const response = await fetch('http://localhost:5000/api/upload', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Failed to fetch graph data');
      }

      const data = await response.json();
      setGraphData(data);
      setCurrentTab(1);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An unknown error occurred');
    }
  };

  const handleTabChange = (event: React.SyntheticEvent, newValue: number) => {
    setCurrentTab(newValue);
  };

  const toggleDrawer = () => {
    setDrawerOpen(!drawerOpen);
  };

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  const drawerContent = (
    <Box sx={{ width: 250 }} role="presentation">
      <List>
        <ListItem>
          <Typography variant="h6" sx={{ p: 2 }}>
            Menu
          </Typography>
        </ListItem>
        <Divider />
        {['Upload', 'Graph', 'Matrix', 'Calendar', 'About'].map((text, index) => (
          <ListItem 
            button 
            key={text}
            onClick={() => {
              setCurrentTab(index);
              setDrawerOpen(false);
            }}
          >
            <ListItemIcon>
              {index === 0 ? <FileUploadIcon /> :
               index === 1 ? <TimelineIcon /> :
               index === 2 ? <TableChartIcon /> :
               index === 3 ? <AssessmentIcon /> :
               <InfoIcon />}
            </ListItemIcon>
            <ListItemText primary={text} />
          </ListItem>
        ))}
      </List>
      <Divider />
      <FormControlLabel
        control={
          <Switch
            checked={darkMode}
            onChange={toggleDarkMode}
            icon={<LightModeIcon />}
            checkedIcon={<DarkModeIcon />}
          />
        }
        label="Dark Mode"
        sx={{ p: 2 }}
      />
    </Box>
  );

  return (
    <ThemeProvider theme={appTheme}>
      <CssBaseline />
      <Box sx={{ flexGrow: 1 }}>
        <AppBar position="fixed">
          <Toolbar>
            <IconButton
              size="large"
              edge="start"
              color="inherit"
              aria-label="menu"
              sx={{ mr: 2 }}
              onClick={toggleDrawer}
            >
              <MenuIcon />
            </IconButton>
            <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
              Graph Scheduling Interface
            </Typography>
            <IconButton color="inherit" onClick={toggleDarkMode}>
              {darkMode ? <LightModeIcon /> : <DarkModeIcon />}
            </IconButton>
          </Toolbar>
        </AppBar>
        <Drawer
          anchor="left"
          open={drawerOpen}
          onClose={toggleDrawer}
        >
          {drawerContent}
        </Drawer>

        <Container maxWidth="lg" sx={{ mt: 10 }}>
          <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
            <Tabs 
              value={currentTab} 
              onChange={handleTabChange}
              variant="scrollable"
              scrollButtons="auto"
            >
              <Tab label="Upload" icon={<FileUploadIcon />} iconPosition="start" />
              <Tab label="Graph" icon={<TimelineIcon />} iconPosition="start" />
              <Tab label="Matrix" icon={<TableChartIcon />} iconPosition="start" />
              <Tab label="Calendar" icon={<AssessmentIcon />} iconPosition="start" />
              <Tab label="About" icon={<InfoIcon />} iconPosition="start" />
            </Tabs>
          </Box>

          {error && (
            <Alert severity="error" sx={{ mt: 2 }}>
              {error}
            </Alert>
          )}

          <Box>
            <Fade in={currentTab === 0}>
              <Box sx={{ display: currentTab === 0 ? 'block' : 'none' }}>
                <TabPanel value={currentTab} index={0}>
                  <Paper sx={{ p: 3 }}>
                    <Typography variant="h5" gutterBottom>
                      Upload Your Graph File
                    </Typography>
                    <Typography variant="body1" paragraph>
                      Upload a text file containing your graph data. The file should follow the required format:
                      each line should contain task number, duration, and dependencies.
                    </Typography>
                    <FileSelector onFileSelect={handleFileSelect} />
                  </Paper>
                </TabPanel>
              </Box>
            </Fade>

            <Fade in={currentTab === 1}>
              <Box sx={{ display: currentTab === 1 ? 'block' : 'none' }}>
                <TabPanel value={currentTab} index={1}>
                  {graphData && (
                    <Paper sx={{ p: 3, position: 'relative' }}>
                      <Typography variant="h5" gutterBottom>
                        Graph Visualization
                      </Typography>
                      <Alert 
                        severity={graphData.hasCircuit ? "error" : "success"} 
                        sx={{ mb: 2 }}
                      >
                        {graphData.hasCircuit 
                          ? "Circuit detected! This is not a valid scheduling graph."
                          : "No circuit detected. This is a valid scheduling graph."}
                      </Alert>
                      <GraphControls
                        zoom={zoom}
                        onZoomChange={setZoom}
                        onCenter={() => {/* Implement center logic */}}
                        viewMode={viewMode}
                        onViewModeChange={setViewMode}
                        showCriticalPath={showCriticalPath}
                        onToggleCriticalPath={() => setShowCriticalPath(!showCriticalPath)}
                      />
                      <Box sx={{ height: '600px' }} ref={graphRef}>
                        <GraphDisplay 
                          data={graphData}
                          zoom={zoom}
                          viewMode={viewMode}
                          showCriticalPath={showCriticalPath}
                        />
                      </Box>
                      {showCriticalPath && (
                        <CriticalPathDisplay
                          criticalPath={graphData.criticalPath.map(id => parseInt(id))}
                          tasks={graphData.tasks.map(task => ({
                            id: parseInt(task.id),
                            duration: task.duration,
                            early: task.early_dates,
                            late: task.late_dates,
                            margin: task.total_margins
                          }))}
                        />
                      )}
                    </Paper>
                  )}
                </TabPanel>
              </Box>
            </Fade>

            <Fade in={currentTab === 2}>
              <Box sx={{ display: currentTab === 2 ? 'block' : 'none' }}>
                <TabPanel value={currentTab} index={2}>
                  {graphData && (
                    <Paper sx={{ p: 3 }} ref={matrixRef}>
                      <Typography variant="h5" gutterBottom>
                        Value Matrix
                      </Typography>
                      <MatrixDisplay matrix={graphData.matrix} />
                    </Paper>
                  )}
                </TabPanel>
              </Box>
            </Fade>

            <Fade in={currentTab === 3}>
              <Box sx={{ display: currentTab === 3 ? 'block' : 'none' }}>
                <TabPanel value={currentTab} index={3}>
                  {graphData && (
                    <Paper sx={{ p: 3 }} ref={calendarRef}>
                      <Typography variant="h5" gutterBottom>
                        Calendar and Margins
                      </Typography>
                      <CalendarDisplay calendar={graphData.calendar} />
                    </Paper>
                  )}
                </TabPanel>
              </Box>
            </Fade>

            <Fade in={currentTab === 4}>
              <Box sx={{ display: currentTab === 4 ? 'block' : 'none' }}>
                <TabPanel value={currentTab} index={4}>
                  <Paper sx={{ p: 3 }}>
                    <Typography variant="h5" gutterBottom>
                      About Graph Scheduling Interface
                    </Typography>
                    <Typography variant="body1" paragraph>
                      This application helps you analyze and visualize scheduling graphs. It provides:
                    </Typography>
                    <ul>
                      <li>Graph visualization with interactive nodes and edges</li>
                      <li>Circuit detection in the graph</li>
                      <li>Value matrix representation</li>
                      <li>Calendar calculations with early dates, late dates, and margins</li>
                      <li>Critical path identification</li>
                    </ul>
                    <Typography variant="body1" paragraph>
                      The interface is designed to be intuitive and user-friendly, helping you understand
                      and analyze your scheduling problems effectively.
                    </Typography>
                  </Paper>
                </TabPanel>
              </Box>
            </Fade>
          </Box>

          {graphData && (
            <Box sx={{ display: 'flex', justifyContent: 'center', mb: 3 }}>
              <PDFExport
                graphData={graphData}
                graphRef={graphRef}
                matrixRef={matrixRef}
                calendarRef={calendarRef}
              />
            </Box>
          )}
        </Container>
      </Box>
    </ThemeProvider>
  );
}

export default App;
