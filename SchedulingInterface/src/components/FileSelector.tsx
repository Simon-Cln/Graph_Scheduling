import React, { useState, useCallback } from 'react';
import { 
    Box, 
    Paper, 
    Typography,
    Button,
    IconButton,
    List,
    ListItem,
    ListItemText,
    ListItemSecondaryAction,
    Divider
} from '@mui/material';
import { styled } from '@mui/material/styles';
import { CloudUpload, Delete, InsertDriveFile } from '@mui/icons-material';

interface FileSelectorProps {
    onFileSelect: (file: File) => void;
}

const DropZone = styled(Paper)(({ theme }) => ({
    padding: theme.spacing(4),
    textAlign: 'center',
    cursor: 'pointer',
    border: `2px dashed ${theme.palette.primary.main}`,
    '&:hover': {
        backgroundColor: theme.palette.action.hover,
    },
}));

const HiddenInput = styled('input')({
    display: 'none',
});

const FileSelector: React.FC<FileSelectorProps> = ({ onFileSelect }) => {
    const [isDragging, setIsDragging] = useState(false);

    const handleDragOver = useCallback((e: React.DragEvent) => {
        e.preventDefault();
        setIsDragging(true);
    }, []);

    const handleDragLeave = useCallback((e: React.DragEvent) => {
        e.preventDefault();
        setIsDragging(false);
    }, []);

    const handleDrop = useCallback((e: React.DragEvent) => {
        e.preventDefault();
        setIsDragging(false);

        const files = e.dataTransfer.files;
        if (files.length > 0) {
            onFileSelect(files[0]);
        }
    }, [onFileSelect]);

    const handleFileInput = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
        const files = e.target.files;
        if (files && files.length > 0) {
            onFileSelect(files[0]);
        }
    }, [onFileSelect]);

    return (
        <Box sx={{ p: 3 }}>
            <DropZone
                onDragOver={handleDragOver}
                onDragLeave={handleDragLeave}
                onDrop={handleDrop}
                sx={{
                    backgroundColor: isDragging ? 'action.hover' : 'background.paper',
                    mb: 3
                }}
            >
                <HiddenInput
                    type="file"
                    accept=".txt"
                    onChange={handleFileInput}
                    id="file-upload"
                />
                
                <CloudUpload sx={{ fontSize: 48, color: 'primary.main', mb: 2 }} />
                
                <Typography variant="h6" gutterBottom>
                    Glissez-déposez votre fichier ici
                </Typography>
                
                <Typography variant="body2" color="text.secondary" paragraph>
                    ou
                </Typography>
                
                <label htmlFor="file-upload">
                    <Button
                        variant="contained"
                        component="span"
                        startIcon={<InsertDriveFile />}
                    >
                        Sélectionner un fichier
                    </Button>
                </label>
            </DropZone>
        </Box>
    );
};

export default FileSelector;
