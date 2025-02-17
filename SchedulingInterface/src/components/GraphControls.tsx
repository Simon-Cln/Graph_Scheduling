import React from 'react';
import { 
    Box, 
    Slider, 
    IconButton, 
    Paper, 
    Typography,
    ToggleButton,
    ToggleButtonGroup
} from '@mui/material';
import {
    ZoomIn,
    ZoomOut,
    CenterFocusStrong,
    FilterList,
    Timeline,
    AccountTree
} from '@mui/icons-material';

interface GraphControlsProps {
    zoom: number;
    onZoomChange: (zoom: number) => void;
    onCenter: () => void;
    viewMode: 'timeline' | 'tree';
    onViewModeChange: (mode: 'timeline' | 'tree') => void;
    showCriticalPath: boolean;
    onToggleCriticalPath: () => void;
}

const GraphControls: React.FC<GraphControlsProps> = ({
    zoom,
    onZoomChange,
    onCenter,
    viewMode,
    onViewModeChange,
    showCriticalPath,
    onToggleCriticalPath
}) => {
    const handleZoomChange = (event: Event, newValue: number | number[]) => {
        onZoomChange(newValue as number);
    };

    const handleViewModeChange = (
        event: React.MouseEvent<HTMLElement>,
        newMode: 'timeline' | 'tree',
    ) => {
        if (newMode !== null) {
            onViewModeChange(newMode);
        }
    };

    return (
        <Paper 
            sx={{ 
                p: 2, 
                position: 'absolute', 
                top: 20, 
                right: 20, 
                zIndex: 1000,
                backgroundColor: 'background.paper',
                borderRadius: 2,
                boxShadow: 3
            }}
        >
            <Box sx={{ width: 200 }}>
                <Typography gutterBottom>Zoom</Typography>
                <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
                    <IconButton onClick={() => onZoomChange(zoom - 0.1)} size="small">
                        <ZoomOut />
                    </IconButton>
                    <Slider
                        value={zoom}
                        onChange={handleZoomChange}
                        min={0.1}
                        max={2}
                        step={0.1}
                        sx={{ mx: 2 }}
                    />
                    <IconButton onClick={() => onZoomChange(zoom + 0.1)} size="small">
                        <ZoomIn />
                    </IconButton>
                </Box>

                <Box sx={{ mb: 2 }}>
                    <IconButton onClick={onCenter} color="primary">
                        <CenterFocusStrong />
                    </IconButton>
                    <IconButton 
                        onClick={onToggleCriticalPath}
                        color={showCriticalPath ? "primary" : "default"}
                    >
                        <FilterList />
                    </IconButton>
                </Box>

                <Typography gutterBottom>View Mode</Typography>
                <ToggleButtonGroup
                    value={viewMode}
                    exclusive
                    onChange={handleViewModeChange}
                    size="small"
                >
                    <ToggleButton value="timeline">
                        <Timeline />
                    </ToggleButton>
                    <ToggleButton value="tree">
                        <AccountTree />
                    </ToggleButton>
                </ToggleButtonGroup>
            </Box>
        </Paper>
    );
};

export default GraphControls;
